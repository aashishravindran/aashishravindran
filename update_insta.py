import instaloader
import re
import os

def update_readme():
    try:
        # 1. Fetch Instagram Posts
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, "shutterquests")
        posts = []
        for post in profile.get_posts():
            img_html = f'<a href="https://www.instagram.com/p/{post.shortcode}/" target="_blank"><img src="{post.url}" width="200" height="200" style="object-fit: cover; border-radius: 10px; margin: 5px;" alt="Instagram photo"/></a>'
            posts.append(img_html)
            if len(posts) == 4: break
        
        grid_html = f"\n<div align=\"center\">\n" + "\n".join(posts) + "\n</div>\n"

        # 2. Update README.md Safely
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Check if markers exist first!
        if "" not in content or "" not in content:
            print("Markers not found. Skipping update to avoid wiping file.")
            return

        # Use a non-greedy regex to only swap what is BETWEEN the markers
        pattern = r"()(.*?)()"
        replacement = rf"\1{grid_html}\3"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme()
