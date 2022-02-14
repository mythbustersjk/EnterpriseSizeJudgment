# EnterpriseSizeJudgment
# 项目背景
本项目依据企业划型相关依据所开发的批量判断脚本
# 说明
## python版本及所使用的python库
python版本：python3.10（其他版本未测试，不保证代码兼容性）  
python库：openpyxl，PyYAML，colorama
## 脚本结构
- ESJ.py（主程序）
- DefaultRange.py（企业划型依据配置程序）
- IndustryJudgment.py（企业所属行业判断程序）
- Value.py（根据行业返回划型标准）
- SizeJudgmentformula.py（划型程序）
- ReturnValue.py（根据行业及标准值调用划型程序，返回划型结果）
- creat_dict.py（将模版字典化）
- template.xlsx（划型数据填写模版）
- DefaultSetting.yaml（程序配置文件）
## 如何使用
1. 可从releases中直接下载项目源码，安装好对应python版本及库后运行后ESJ.py
2. 可从releases中下载以构建好的ESJ.exe，DefaultSetting.yaml以及template.xlsx。放置同一文件夹中运行ESJ.exe
## License
GPL-3.0 License
