# Sample Codes to read YAML files

**Python**
```python
import yaml

with open('../1.எழுத்ததிகாரம்/1.எழுத்தியல்.yaml' ,encoding='utf8') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data) 
```	

**Convert to Json/XML**  
https://codebeautify.org/yaml-to-json-xml-csv
