from xlwings import Workbook, Sheet, Range, Chart
wb = Workbook('Book2')  # Creates a connection with the active workbook

def cell_word_count(current_cell_value):
    comment_word_count=0
    word_list=[]
    word_count=[]
    comment_length = len(current_cell_value)
    while comment_word_count<comment_length:
        current_word = current_cell_value[comment_word_count].upper()
        if len(word_list)==0:
            word_list.append(current_word)
            word_count.append(1)
            comment_word_count+=1
        else:
            list_loop=0
            while list_loop<len(word_list):
                testing_word = word_list[list_loop].upper()
                if testing_word<>current_word:
                    if list_loop==len(word_list)-1:
                        word_list.append(current_word)
                        word_count.append(1)
                        comment_word_count+=1
                        break
                    else:
                        list_loop+=1
                elif testing_word==current_word:
                    word_count[list_loop] = word_count[list_loop]+1
                    list_loop+=1
                    comment_word_count+=1
                    break
    return word_list, word_count



def test_cells():
    cells=Range('C6:C441').value
    count=0
    master_text=[]
    while count<len(cells):
        if isinstance(cells[count],basestring):
            current_cell = cells[count].split(" ")
            current_text_count=0
            while current_text_count<len(current_cell):
                master_text.append(current_cell[current_text_count])
                current_text_count+=1
            count+=1
        else:
            count+=1
    return cell_word_count(master_text)


Range('X3').value= test_cells()

print test_cells()


