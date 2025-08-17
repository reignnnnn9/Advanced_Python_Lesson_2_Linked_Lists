from linked_list import LinkedList, Node

class Song:
    def __init__(self, title, artist, duration):
        self.title = title      # Song title
        self.artist = artist    # Artist name
        self.duration = duration  # Duration in seconds
    
    def __str__(self):
        """Format as 'Title by Artist (MM:SS)'"""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"

class MusicPlaylist:
    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()      # Use our LinkedList to store songs
        self.current_position = -1     # Track current song (-1 = not playing)
    
    def add_song(self, title, artist, duration):
        """Add a song to the end of the playlist - ALREADY IMPLEMENTED"""
        song = Song(title, artist, duration)  # Create Song object
        self.songs.append(song)                # Add to linked list
        print(f"Added: {song}")
    
    def display_playlist(self):
        """Show all songs in the playlist - ALREADY IMPLEMENTED"""
        print(f"\nPlaylist: {self.name}")
        print("-" * 60)
        
        if self.songs.is_empty():
            print("No songs in playlist")
            return
        
        # Traverse and display each song
        current = self.songs.head
        position = 0
        
        while current:
           #Displaying data of song currently looping over
            print(f"{position + 1}. {current.data}")
            current = current.next  # Move to next song
            position += 1           # Increment counter
        
        print("-" * 60)
    
    # YOUR IMPLEMENTATIONS START HERE
    
    def play_song_at_position(self, position): # Takes in 1-based position
        index = position - 1 # Converts to 0-based position
        song = self.songs.get_at_position(index) # Utilizes our LinkedList method 
        self.current_position = index
        print(f"Now playing: {song.title}")
        return song
    
    def next_song(self):
        next_index = self.current_position + 1
        next_song = self.songs.get_at_position(next_index)
        self.current_position = next_index
        print(f"Now playing next song: {next_song.title}")
        return next_song
    
    def previous_song(self):
        prev_index = self.current_position - 1
        prev_song = self.songs.get_at_position(prev_index)
        self.current_position = prev_index
        print(f"Now playing previous song: {prev_song.title}")
        return prev_song
    
    def remove_current_song(self):
        removing = self.songs.delete_at_position(self.current_position)
        print(f"Removed Song: {removing.data.title}")
    
    def find_songs_by_artist(self, artist_name):
        """
        Find all songs by a specific artist        
        Args:
            artist_name: Name of the artist to search for        
        Returns:
            List of song titles by that artist        
        Example:
            queen_songs = playlist.find_songs_by_artist("Queen")
            print(f"Queen songs: {queen_songs}")
        """
        # Todo: Implement this method (BONUS)
        # Steps:
        # 1. Create empty list to store matching song titles
        # 2. Traverse the linked list
        # 3. For each song, check if artist matches (case-insensitive)
        # 4. Add matching song titles to the list
        # 5. Return the list

# ==========================================================================

# Test your playlist implementation
def test_music_playlist():
    """Test function to verify your MusicPlaylist methods work correctly"""
    print("Testing Music Playlist Implementation...")
    
    # Create a playlist and add songs
    playlist = MusicPlaylist("My Awesome Mix")
    
    # Add test songs (title, artist, duration_in_seconds)
    playlist.add_song("Bohemian Rhapsody", "Queen", 355)        # 5:55
    playlist.add_song("Stairway to Heaven", "Led Zeppelin", 482)  # 8:02
    playlist.add_song("Hotel California", "Eagles", 391)         # 6:31
    playlist.add_song("We Will Rock You", "Queen", 122)         # 2:02
    playlist.add_song("Sweet Child O' Mine", "Guns N' Roses", 356)  # 5:56
    
    # Display initial playlist
    playlist.display_playlist()
    
    # Test playing a specific song
    print("\n--- Testing play_song_at_position ---")
    try:
        song = playlist.play_song_at_position(2)  # Play second song
        if song:
            print(f"Now playing: {song}")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in play_song_at_position: {e}")
    
    # Test navigation
    print("\n--- Testing next_song ---")
    try:
        next_song = playlist.next_song()
        if next_song:
            print(f"Next song: {next_song}")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in next_song: {e}")
    
    print("\n--- Testing previous_song ---")
    try:
        prev_song = playlist.previous_song()
        if prev_song:
            print(f"Previous song: {prev_song}")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in previous_song: {e}")
    
        # Test finding songs by artist (bonus)
    print("\n--- Testing find_songs_by_artist (BONUS) ---")
    try:
        queen_songs = playlist.find_songs_by_artist("Queen")
        print(f"Songs by Queen: {queen_songs}")
    except Exception as e:
        print(f"Error in find_songs_by_artist: {e}")
    
    # Test removing current song
    print("\n--- Testing remove_current_song ---")
    try:
        print(f"Before removal:")
        playlist.display_playlist()
        
        removed = playlist.remove_current_song()
        if removed:
            print("Song removed successfully")
        
        print(f"After removal:")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in remove_current_song: {e}")
    
    print("\n✅ Test completed!")

# Uncomment to test your implementation
test_music_playlist()

# ==========================================================================

# Test from class recording
# playlist = MusicPlaylist("My Awesome Mix")
# playlist.add_song("Bohemian Rhapsody", "Queen", 355)        # 5:55
# playlist.add_song("Stairway to Heaven", "Led Zeppelin", 482)  # 8:02
# playlist.add_song("Hotel California", "Eagles", 391)         # 6:31
# playlist.add_song("We Will Rock You", "Queen", 122)         # 2:02
# playlist.add_song("Sweet Child O' Mine", "Guns N' Roses", 356) 

# playlist.display_playlist()
# selected_song = playlist.play_song_at_position(3)
# next_song = playlist.next_song()
# playlist.previous_song()
# playlist.remove_current_song()
# playlist.display_playlist()