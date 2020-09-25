from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for ele in attrs:
            print (f'-> {ele[0]} > {ele[1]}')
        
    def handle_endtag(self, tag):
        pass
        
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for ele in attrs:
            print (f'-> {ele[0]} > {ele[1]}')
        

parser = MyHTMLParser()

parser.feed(''.join([input().strip() for _ in range(int(input()))]))

