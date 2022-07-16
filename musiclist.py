class MusicNode:
    def __init__(self, song_name = None, next_music = None):
        self.song_name = song_name
        self.next_music = next_music

class MusicList:
    def __init__(self):  
        self.head = None
    def printMusic(self): 
        value = self.head 
        while (value): 
            print(value.song_name) 
            value = value.next_music
if __name__=='__main__':
    #initialize linked list object
    linked_list = MusicList()
    print(linked_list)

    #assign values to nodes 
    linked_list.head = MusicNode("A Hard Day's Night")
    second = MusicNode('A Day in the Life')
    third = MusicNode("Strawberry Fields Forever")

    #link nodes
    linked_list.head.next_music = second

    second.next_song = third

    linked_list.printMusic()