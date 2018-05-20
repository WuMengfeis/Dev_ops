#!/bin/sh
# this is my first shell
echo "git add ."
git add .
echo "git commit"
echo "请输入commit的注释信息："
read comment
git commit -m "$comment"
echo "git push origin master"
git push origin master
