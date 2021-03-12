import re

class FileAnalyzer:
    def __init__(self,file,content):
        self.filename = file
        self.content = content
    
    def readPHPString(self):
        php_pattern = re.compile(r'(<\?php.*?\?>)',re.DOTALL)
        value = php_pattern.finditer(self.content)
        content=[]
        for match in value:
            content.append(match.group(0))
        return content
            # break