import os
import glob

def build(filepath: str, output_dir: str, template_path: str):
    os.system(f"jupyter nbconvert {filepath} --to=html --output-dir={output_dir} --template-file={template_path}")

if __name__ == "__main__":
    posts = glob.glob("./posts/active/*.ipynb")
    for p in posts:
        if p.endswith("index.ipynb"):
            build(p, "./site", "index.jinja2")
        else:
            build(p, "./site/html", "template.jinja2")