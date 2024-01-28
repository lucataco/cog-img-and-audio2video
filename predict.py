# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
from moviepy.editor import ImageClip, AudioFileClip

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def predict(
        self,
        image: Path = Input(description="Grayscale input image"),
        audio: Path = Input(description="Audio file"),
    ) -> Path:
        """Run a single prediction on the model"""
        audio_path = str(audio)
        audio_clip = AudioFileClip(audio_path)
        # Create a video clip with the image, matching the audio duration
        image_path = str(image)
        video_clip = ImageClip(image_path, duration=audio_clip.duration)
        # Set the audio of the video clip as the audio clip
        video_clip = video_clip.set_audio(audio_clip)

        output_path = "/tmp/output.mp4"
        video_clip.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')

        return Path(output_path)
