# converT a MP4 to mp3 file
import moviepy.editor
video = moviepy.editor.VideoFileClip("2020-10-21_EDM_dj946666a_Clip 59.mp4")
audio =video.audio
audio.write_audiofile("2020-10-21_EDM_dj946666a_Clip 59.mp3")
