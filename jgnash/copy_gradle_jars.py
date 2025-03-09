import os
import shutil

# Define the source and destination paths
gradle_cache_dir = os.path.expanduser("~/.gradle/caches/modules-2/files-2.1")  # Windows & Linux
project_libs_dir = os.path.join(os.getcwd(), "libs")  # Creates a "libs" folder in the current project

# Ensure the destination "libs" directory exists
os.makedirs(project_libs_dir, exist_ok=True)

# Walk through the Gradle cache directory to find all .jar files
jar_files = []
for root, _, files in os.walk(gradle_cache_dir):
    for file in files:
        if file.endswith(".jar"):
            jar_files.append(os.path.join(root, file))

# Copy the found JAR files to the "libs" directory
for jar in jar_files:
    dest_file = os.path.join(project_libs_dir, os.path.basename(jar))  # Copy with just the filename
    if not os.path.exists(dest_file):  # Prevent overwriting existing files
        shutil.copy2(jar, dest_file)
        print(f"Copied: {jar} -> {dest_file}")
    else:
        print(f"Skipped (already exists): {dest_file}")

print(f"\n Done! {len(jar_files)} JAR files processed. Check the 'libs/' directory.")
