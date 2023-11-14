# Update the variable called dracula_text that is the result of calling the get_text method on the dracula_text variable
with open('HW7_Files\Dracula.txt', 'r', encoding='utf-8') as D:
    dracula_text = D.read()
#pathway to dracula text file


def get_text(text):
    start = text.find('*** START OF THIS PROJECT GUTENBERG EBOOK DRACULA ***')
    end = text.find('*** END OF THIS PROJECT GUTENBERG EBOOK DRACULA ***')
    return text[end:start]

print 
print(get_text(dracula_text))


dracula_text_list = get_text(dracula_text)
print(dracula_text_list)
print("testing ")