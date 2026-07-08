from pathlib import Path
from llama_cloud import LlamaCloud
import os

client = LlamaCloud(os.getenv(LLAMA_CLOUD_API))

PDF_PATH = "PDF_RAG_Pipeline/sample-tables.pdf"

file_obj = client.files.create(file="/home/rogue/RAG/PDF_RAG_Pipeline/sample-tables.pdf", purpose="parse")


result = client.parsing.parse(
    file_id=file_obj.id,
    
    tier="agentic",
    

    version="latest",
    output_options = {
            "markdown":
        {
            "annotate_links" : True,
            "inline_images": True,
            
        }},
        expand=["markdown_full"],
        
    )

# result = client.parsing.parse(
#     file_id=file_obj.id,
#     tier="agentic",
#     version="latest",
#     output_options={
#         "markdown": {
#             "tables": {
#                 "output_tables_as_markdown": True
#             }
#         }
#     },
#     expand=["markdown"],
# )
# Persist markdown and text to disk
Path("output5.md").write_text(result.markdown_full or "")
# Path("output4.txt").write_text(result.text_full or "")
# Path("output.pdf").write_text(result.output_pdf_content_metadata or "")
print(f"Wrote {len(result.markdown_full or '')} chars of markdown")

# def parse_pdf_to_markdown_pages(pdf_path: str):
#     """Upload a PDF to LlamaCloud Parse and return page objects with a .text attribute."""
    # file_obj = client.files.create(file=pdf_path, purpose="parse")


#     markdown_pages = getattr(getattr(result, "markdown", None), "pages", None)
#     if not markdown_pages:
#         raise ValueError("Parse completed but returned no markdown pages.")

#     parsed_pages = []
#     for idx, page in enumerate(markdown_pages, 1):
#         page_number = getattr(page, "page_number", idx)
#         markdown_text = getattr(page, "markdown", "") or ""
#         parsed_pages.append(SimpleNamespace(text=markdown_text, metadata={"page": page_number}))
#     return parsed_pages


# parsed_documents = parse_pdf_to_markdown_pages(PDF_PATH)

# print(f"Parsing complete!")
# print(f"Number of pages: {len(parsed_documents)}")
# print(f"Total characters: {sum(len(doc.text) for doc in parsed_documents):,}")