import os
import requests
from dotenv import load_dotenv, find_dotenv

# .envファイルが存在する場合のみ読み込む
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
PAGE_ID = os.getenv('PAGE_ID')

# デバッグ出力
print(f"NOTION_API_KEY: {NOTION_API_KEY}")
print(f"PAGE_ID: {PAGE_ID}")

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_page_content(page_id):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")
    return response.json()

def notion_to_markdown(content):
    markdown = ""
    for block in content["results"]:
        block_type = block["type"]

        if block_type == "paragraph":
            text = block["paragraph"]["rich_text"]
            markdown += "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "heading_1":
            text = block["heading_1"]["rich_text"]
            markdown += "# " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "heading_2":
            text = block["heading_2"]["rich_text"]
            markdown += "## " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "heading_3":
            text = block["heading_3"]["rich_text"]
            markdown += "### " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "bulleted_list_item":
            text = block["bulleted_list_item"]["rich_text"]
            markdown += "- " + "".join([t["plain_text"] for t in text]) + "\n"

        elif block_type == "numbered_list_item":
            text = block["numbered_list_item"]["rich_text"]
            markdown += "1. " + "".join([t["plain_text"] for t in text]) + "\n"

        elif block_type == "quote":
            text = block["quote"]["rich_text"]
            markdown += "> " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "code":
            text = block["code"]["rich_text"]
            language = block["code"]["language"]
            markdown += f"```{language}\n" + "".join([t["plain_text"] for t in text]) + "\n```\n\n"

        elif block_type == "image":
            image_url = block["image"]["file"]["url"]
            markdown += f"![image]({image_url})\n\n"

        elif block_type == "bookmark":
            bookmark_url = block["bookmark"]["url"]
            markdown += f"[Bookmark]({bookmark_url})\n\n"

        # Add more block types as needed

    return markdown

content = get_page_content(PAGE_ID)
markdown_content = notion_to_markdown(content)

# Save the markdown content with utf-8 encoding
with open("exported_document.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("Markdown export complete.")
