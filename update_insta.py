import instaloader
import re
import os

def update_readme():
    # 1. Fetch Instagram Posts
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, "shutterquests")
        posts = []
        for post in profile.get_posts():
            # We want the display URL (image) and the post URL
            img_html = f'<a href="https://www.instagram.com/p/{post.shortcode}/" target="_blank"><img src="{post.url}" width="200" height="200" style="object-fit: cover; border-radius: 10px; margin: 5px;" alt="Instagram photo"/></a>'
            posts.append(img_html)
            if len(posts) == 4: # Grab the latest 4
                break
        
        grid_html = "\n".join(posts)

        # 2. Update README.md
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find our markers and swap the content
        pattern = r".*?"
        replacement = f"\n<div align=\"center\">\n{grid_html}\n</div>\n"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
            
    except Exception as e:
        print(f"Error fetching Instagram: {e}")

if __name__ == "__main__":
    update_readme()
