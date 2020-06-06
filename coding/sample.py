# coding=utf-8
# Copyright (c) 2020 பதம்.org team
import yaml

with open('../1.எழுத்ததிகாரம்/2.பதவியல்.yaml' ,encoding='utf8') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
	