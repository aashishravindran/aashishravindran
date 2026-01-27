import instaloader
import os

def update_readme():
    L = instaloader.Instaloader()
    try:
        # 1. Fetch Instagram Posts
        profile = instaloader.Profile.from_username(L.context, "shutterquests")
        posts = []
        for post in profile.get_posts():
            # Use post.url for the image src
            img_html = f'<a href="https://www.instagram.com/p/{post.shortcode}/" target="_blank"><img src="{post.url}" width="200" height="200" style="object-fit: cover; border-radius: 10px; margin: 5px;" alt="Instagram photo"/></a>'
            posts.append(img_html)
            if len(posts) == 4: break
        
        grid_content = f"\n<div align=\"center\">\n" + "\n".join(posts) + "\n</div>\n"

        # 2. Update README.md using Split logic (much safer than Regex)
        with open("README.md", "r", encoding="utf-8") as f:
            full_text = f.read()

        start_marker = ""
        end_marker = ""

        if start_marker not in full_text or end_marker not in full_text:
            print("Markers missing!")
            return

        # Split the file into three parts: Before, Middle (to be discarded), and After
        before_part = full_text.split(start_marker)[0]
        after_part = full_text.split(end_marker)[1]

        # Reconstruct the file
        new_readme = before_part + start_marker + grid_content + end_marker + after_part

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_readme)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme()
