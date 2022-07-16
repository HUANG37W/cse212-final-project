class SongNode:
    def __init__(self, current_song=None, next_song = None):
        self.current_song = current_song
        self.next_song = next_song

class SongList: 
    def __init__(self):  
        self.head = None
    def printSongs(self): 
        value = self.head 
        while (value): 
            print(value.current_song) 
            value = value.next_song
            
    def newSong(self, new_song):
        NewSongNode = SongNode(new_song)
        if self.head is None:
            self.head = NewSongNode           
        last = self.head
        while(last.next_song):
            last = last.next_song
        last.next_song=NewSongNode
   

if __name__=='__main__':
    #initialize linked list object
    linked_list = SongList()
    print(linked_list)


 
    #assign values to nodes 
    linked_list.head = SongNode("A Hard Day's Night")
    second = SongNode('A Day in the Life')
    third = SongNode("Strawberry Fields Forever")
    

    #link nodes
    linked_list.head.next_song = second
    second.next_song = third

    linked_list.newSong("She Loves You")
    linked_list.newSong("Something")
    linked_list.printSongs()