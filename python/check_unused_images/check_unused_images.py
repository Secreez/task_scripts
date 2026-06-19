import os
import re
from datetime import datetime

project_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
images_folder = os.path.join(project_folder, "images")
log_file_path = os.path.join(project_folder, "unused_images.log")

image_extensions = (".jpg", ".jpeg", ".png", ".svg")


def get_referenced_images(files, file_extension):
    """Extract all referenced image filenames from RMD or QMD files."""
    referenced_images = set()

    rmd_pattern = re.compile(r"(?:include_graphics\(['\"])(.*?)(['\"])")
    qmd_pattern = re.compile(r"!\[.*?\]\((.*?\.(?:png|jpg|jpeg|svg))\)", re.IGNORECASE)

    for file in files:
        print(f"Checking file: {os.path.basename(file)}")
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            if file_extension.lower() == ".rmd":
                matches = rmd_pattern.findall(content)
            elif file_extension.lower() == ".qmd":
                matches = qmd_pattern.findall(content)

            if matches:
                print(
                    f"  Found {len(matches)} matches: {', '.join([os.path.basename(match[0] if isinstance(match, tuple) else match) for match in matches])}"
                )
            else:
                print("  No matches found.")

            for match in matches:
                image_path = os.path.normpath(
                    match[0] if isinstance(match, tuple) else match
                )
                referenced_images.add(os.path.basename(image_path))
    return referenced_images


def get_existing_images(images_folder):
    """Get all image filenames in the images folder."""
    # Case-insensitive extension check, so files like 'performance.PNG' are
    # picked up too (str.endswith() is case-sensitive by default).
    existing_images = {
        img
        for img in os.listdir(images_folder)
        if img.lower().endswith(image_extensions)
    }
    print("\nExisting images in folder:")
    print(
        f"  Found {len(existing_images)} images (showing first 10): {', '.join(list(existing_images)[:10])}..."
    )
    return existing_images


def detect_file_types():
    """Detect all .Rmd and .qmd files in the project.

    Intentionally only scans the top level of project_folder (no recursion
    into subfolders). This is by design: it avoids picking up stray .qmd
    files that got copy-pasted in from older versions/branches and would
    otherwise pollute the "referenced images" set.
    """
    rmd_files = [
        os.path.join(project_folder, f)
        for f in os.listdir(project_folder)
        if f.lower().endswith(".rmd")
    ]
    qmd_files = [
        os.path.join(project_folder, f)
        for f in os.listdir(project_folder)
        if f.lower().endswith(".qmd")
    ]

    print("\nDetected file types:")
    if rmd_files:
        print(f"  {len(rmd_files)} .Rmd files detected.")
    if qmd_files:
        print(f"  {len(qmd_files)} .qmd files detected.")
    if not rmd_files and not qmd_files:
        print("  No .Rmd or .qmd files found.")
    return rmd_files, qmd_files


def main():
    rmd_files, qmd_files = detect_file_types()
    if not rmd_files and not qmd_files:
        print("No valid files to check. Exiting...")
        return

    referenced_images = set()

    if rmd_files:
        print("\nProcessing .Rmd files...")
        referenced_images.update(get_referenced_images(rmd_files, ".rmd"))
    if qmd_files:
        print("\nProcessing .qmd files...")
        referenced_images.update(get_referenced_images(qmd_files, ".qmd"))

    existing_images = get_existing_images(images_folder)

    print("\nReferenced images:")
    print(
        f"  Found {len(referenced_images)} referenced images: {', '.join(list(referenced_images)[:10])}..."
    )

    # Case-insensitive comparison: build a lookup from lowercased filename
    # back to the original filename, so 'Performance.PNG' referenced as
    # 'performance.png' in a .qmd still matches correctly.
    existing_by_lower = {img.lower(): img for img in existing_images}
    referenced_lower = {img.lower() for img in referenced_images}

    unused_images = sorted(
        existing_by_lower[lower_name]
        for lower_name in existing_by_lower
        if lower_name not in referenced_lower
    )
    total_images = len(existing_images)

    with open(log_file_path, "w", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"Unused Images Log\nGenerated on: {timestamp}\n\n")
        log_file.write(f"Total images in folder: {total_images}\n")
        log_file.write(f"Total unused images: {len(unused_images)}\n\n")
        log_file.write("------------------------------------\n\n")
        for image in unused_images:
            log_file.write(f"{image}\n")

    print("\nCheck completed!")
    print(f"  Unused images logged in: {log_file_path}")


if __name__ == "__main__":
    main()
