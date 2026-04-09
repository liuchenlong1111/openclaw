#!/usr/bin/env node

/**
 * ossutil 上传脚本
 * 用法: node upload.js <local-file> <bucket> [object-name]
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

function printUsage() {
  console.log(`
ossutil-upload - 上传文件到阿里云 OSS

用法:
  node upload.js <local-file> <bucket> [object-name]

参数:
  local-file   本地文件路径 (必需)
  bucket       OSS 存储桶名称 (必需，不需要 oss:// 前缀)
  object-name  OSS 对象名称 (可选，默认使用本地文件名)

示例:
  node upload.js /path/to/file.jpg my-bucket
  node upload.js /path/to/local.jpg my-bucket remote.jpg
`);
}

function main() {
  const args = process.argv.slice(2);
  
  if (args.length < 2) {
    printUsage();
    process.exit(1);
  }
  
  const localFile = args[0];
  const bucket = args[1];
  let objectName = args[2];
  
  // 如果没有指定对象名，使用本地文件名
  if (!objectName) {
    objectName = path.basename(localFile);
  }
  
  // 检查本地文件是否存在
  if (!fs.existsSync(localFile)) {
    console.error(`错误: 文件不存在 - ${localFile}`);
    process.exit(1);
  }
  
  const ossPath = `oss://${bucket}/${objectName}`;
  const command = `ossutil cp "${localFile}" "${ossPath}"`;
  
  console.log(`正在上传: ${localFile} -> ${ossPath}`);
  console.log(`执行命令: ${command}`);
  console.log('---');
  
  try {
    const output = execSync(command, { encoding: 'utf8', stdio: 'inherit' });
    console.log('---');
    console.log('✅ 上传成功');
    console.log(`  本地文件: ${localFile}`);
    console.log(`  OSS 路径: ${ossPath}`);
    
    // 获取文件信息
    const stats = fs.statSync(localFile);
    console.log(`  文件大小: ${stats.size} 字节`);
    
    process.exit(0);
  } catch (error) {
    console.error('---');
    console.error('❌ 上传失败');
    console.error(`错误: ${error.message}`);
    process.exit(1);
  }
}

main();
