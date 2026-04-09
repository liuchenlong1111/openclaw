#!/usr/bin/env node

/**
 * Whisper Transcribe + OSS Upload Agent
 *
 * 功能：
 * 1. 使用 whisper 转录音视频文件生成字幕/文本
 * 2. 将所有输出文件上传到指定 OSS bucket
 * 3. 返回可下载的 OSS 地址
 *
 * 用法:
 *   node transcribe-and-upload.js <input-file> <bucket> [options]
 *
 * 参数:
 *   input-file    输入音视频文件路径 (必需)
 *   bucket        OSS 存储桶名称 (必需)
 *
 * 选项:
 *   --language <lang>    语言 (默认: zh 中文)
 *   --model <model>      模型大小 (默认: medium)
 *   --format <format>    输出格式 (默认: all，可选 txt,vtt,srt,json,tsv)
 *   --output-dir <dir>   输出目录 (默认: ./output)
 */

const { execSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const OSS_UPLOAD_SCRIPT = '/Users/liuchenglong/.openclaw/workspace/skills/ossutil-upload/scripts/upload.js';

function printUsage() {
  console.log(`
Whisper Transcribe + OSS Upload Agent

功能:
  1. 使用 OpenAI Whisper 转录音视频文件
  2. 将转录结果上传到阿里云 OSS
  3. 返回可下载的 OSS 链接

用法:
  node transcribe-and-upload.js <input-file> <bucket> [options]

参数:
  input-file    输入音视频文件路径 (必需)
  bucket        OSS 存储桶名称 (必需)

选项:
  --language <lang>    语言代码，默认 zh (中文)
  --model <model>      Whisper 模型大小，默认 medium (tiny|base|small|medium|large)
  --format <format>    输出格式，默认 all (txt|vtt|srt|json|tsv|all)
  --output-dir <dir>   本地输出目录，默认 ./whisper-output

示例:
  # 转录中文音频，上传到 whisper-transcribe bucket
  node transcribe-and-upload.js ~/Downloads/audio.mp3 whisper-transcribe

  # 使用 large 模型转录英文
  node transcribe-and-upload.js ~/video.mp4 my-bucket --language en --model large
`);
}

function checkDependencies() {
  // 检查 whisper
  try {
    execSync('which whisper', { stdio: 'ignore' });
  } catch (e) {
    console.error('❌ 错误: whisper 命令未找到，请先安装 OpenAI Whisper');
    console.error('   pip install openai-whisper');
    process.exit(1);
  }

  // 检查 ffmpeg
  try {
    execSync('which ffmpeg', { stdio: 'ignore' });
  } catch (e) {
    console.error('❌ 错误: ffmpeg 命令未找到，请先安装 ffmpeg');
    console.error('   brew install ffmpeg');
    process.exit(1);
  }

  // 检查 ossutil
  try {
    execSync('which ossutil', { stdio: 'ignore' });
  } catch (e) {
    console.error('❌ 错误: ossutil 命令未找到，请先安装并配置 ossutil');
    process.exit(1);
  }

  // 检查上传脚本
  if (!fs.existsSync(OSS_UPLOAD_SCRIPT)) {
    console.error(`❌ 错误: ossutil-upload 脚本未找到 - ${OSS_UPLOAD_SCRIPT}`);
    process.exit(1);
  }
}

function main() {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    printUsage();
    process.exit(1);
  }

  checkDependencies();

  const inputFile = path.resolve(args[0]);
  const bucket = args[1];

  // 默认配置
  let options = {
    language: 'zh',
    model: 'medium',
    format: 'all',
    outputDir: path.resolve('./whisper-output'),
  };

  // 解析选项
  for (let i = 2; i < args.length; i += 2) {
    const key = args[i];
    const value = args[i + 1];
    switch (key) {
      case '--language':
        options.language = value;
        break;
      case '--model':
        options.model = value;
        break;
      case '--format':
        options.format = value;
        break;
      case '--output-dir':
        options.outputDir = path.resolve(value);
        break;
      default:
        console.error(`⚠️  未知选项: ${key}`);
        break;
    }
  }

  // 检查输入文件
  if (!fs.existsSync(inputFile)) {
    console.error(`❌ 错误: 输入文件不存在 - ${inputFile}`);
    process.exit(1);
  }

  // 创建输出目录
  if (!fs.existsSync(options.outputDir)) {
    console.log(`📁 创建输出目录: ${options.outputDir}`);
    fs.mkdirSync(options.outputDir, { recursive: true });
  }

  const inputBaseName = path.basename(inputFile, path.extname(inputFile));
  console.log(`
============================================================
📝 开始处理
   输入文件: ${inputFile}
   OSS Bucket: ${bucket}
   语言: ${options.language}
   模型: ${options.model}
   输出格式: ${options.format}
   输出目录: ${options.outputDir}
============================================================
`);

  // 构建 whisper 命令
  let whisperCmd = `whisper "${inputFile}"`;
  whisperCmd += ` --language ${options.language}`;
  whisperCmd += ` --model ${options.model}`;
  whisperCmd += ` --output_dir "${options.outputDir}"`;
  if (options.format !== 'all') {
    whisperCmd += ` --output_format ${options.format}`;
  }

  console.log(`🔊 执行 Whisper 转录...`);
  console.log(`   命令: ${whisperCmd}`);
  console.log('');

  try {
    // 执行 whisper
    execSync(whisperCmd, { encoding: 'utf8', stdio: 'inherit' });
  } catch (error) {
    console.error('\n❌ 转录失败');
    console.error(error.message);
    process.exit(1);
  }

  console.log(`
✅ 转录完成，开始上传到 OSS...
`);

  // 获取所有输出文件
  const outputFiles = [];
  const formats = options.format === 'all'
    ? ['txt', 'vtt', 'srt', 'json', 'tsv']
    : [options.format];

  formats.forEach(fmt => {
    const outputFile = path.join(options.outputDir, `${inputBaseName}.${fmt}`);
    if (fs.existsSync(outputFile)) {
      outputFiles.push(outputFile);
    }
  });

  if (outputFiles.length === 0) {
    console.error('❌ 错误: 没有找到输出文件');
    process.exit(1);
  }

  console.log(`📦 找到 ${outputFiles.length} 个输出文件需要上传`);

  // 逐个上传
  const uploadedUrls = [];
  const ossResults = [];

  outputFiles.forEach(localFile => {
    const fileName = path.basename(localFile);
    const objectName = `transcripts/${inputBaseName}/${fileName}`;

    console.log(`⬆️  上传 ${fileName}...`);

    const uploadCmd = `node "${OSS_UPLOAD_SCRIPT}" "${localFile}" "${bucket}" "${objectName}"`;

    try {
      execSync(uploadCmd, { encoding: 'utf8', stdio: 'inherit' });
      const ossUrl = `oss://${bucket}/${objectName}`;
      uploadedUrls.push(ossUrl);
      ossResults.push({
        localFile,
        ossUrl,
        size: fs.statSync(localFile).size,
      });
      console.log(`✅ ${fileName} 上传成功`);
    } catch (error) {
      console.error(`❌ ${fileName} 上传失败`);
    }
  });

  console.log(`
============================================================
🎉 全部完成！
============================================================

📊 统计信息:
   输入文件: ${inputFile}
   输出文件数: ${uploadedUrls.length}/${outputFiles.length}
   输出目录: ${options.outputDir}

📥 OSS 地址列表:
`);

  uploadedUrls.forEach(url => {
    console.log(`   ${url}`);
  });

  // 如果 OSS bucket 开启了公共访问，可以生成 HTTPS URL
  // 用户可以根据自己的域名配置生成
  console.log(`
🔗 如果你开启了公共读，可以通过 HTTPS 访问:
   https://${bucket}.oss-cn-hangzhou.aliyuncs.com/transcripts/${inputBaseName}/{filename}
`);

  // 保存结果 JSON 文件
  const resultJson = {
    inputFile,
    bucket,
    options,
    timestamp: new Date().toISOString(),
    results: ossResults,
  };

  const resultFile = path.join(options.outputDir, `${inputBaseName}.result.json`);
  fs.writeFileSync(resultFile, JSON.stringify(resultJson, null, 2));
  console.log(`📄 结果已保存到: ${resultFile}`);

  console.log('');
}

main();
