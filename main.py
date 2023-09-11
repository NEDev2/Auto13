import requests
import subprocess
import os

def download_video(url, filename):
    """Download video from the given URL."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192): 
            f.write(chunk)


def main():
    base_url = "https://cfvod.kaltura.com/scf/enc/hls/p/2748741/sp/274874100/serveFlavor/entryId/0_330v9kzz/v/2/ev/6/flavorId/0_kb3o315o/name/a.mp4/seg-{segment}-v1-a1.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvZW5jL2hscy9wLzI3NDg3NDEvc3AvMjc0ODc0MTAwL3NlcnZlRmxhdm9yL2VudHJ5SWQvMF8zMzB2OWt6ei92LzIvZXYvNi9mbGF2b3JJZC8wX2tiM28zMTVvL25hbWUvYS5tcDQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY5NDQ1MzM3MH19fV19&Signature=P2ZKqeMZjZuhCwMtY4VTgIzZZFJCZbZ8hSBe9NiTnp8b4V9pxKwTJwaOFhdewA-zioOrZZTktazpYAjiB5Q-MVZueTnHPc9MyBRwg4X08GVUvcknQ7ogrs0gxvKJNZlxSKUXvyRHlpXfMFbC5URwPoTUsD~LlFMaCs-9ZlK14JP8ddYHx51Q~DyKGZuDOPFo82sjnrHVhwMwXhdRk2KVk8x0UGJVJRVtEsZcZ5X502jyuQRz1E8rxLF6opNZwypVN1E2gRMH6-Oi3BqplYGDiZP68GMXfiQeYRe6VUTRasq4Iiemt~qGOaGao50VkDfisoqxEVK676Wapf2wAQ~0Eg__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A"

    downloaded_files = []
    part = 1

    while True:
        url = base_url.format(segment=part)
        filename = f"video_part_{part}.ts"
        
        try:
            print(f"Downloading part {part}...")
            download_video(url, filename)
            
            # Check if the downloaded file is empty
            if os.path.getsize(filename) == 0:
                os.remove(filename)
                print(f"Part {part} is empty. Stopping download.")
                break
            
            downloaded_files.append(filename)
            part += 1

        except requests.RequestException:
            print(f"Failed to download part {part}. Stopping download.")
            break



    print("Process complete!")

if __name__ == "__main__":
    main()