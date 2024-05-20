#from  lvis import LVIS
import json

# # Path to the LVIS annotations file
# lvis_annotation_path = 'path/to/lvis_v1_train.json'

# # Load the LVIS dataset
# lvis = LVIS(lvis_annotation_path)

# # Get the list of categories
# categories = lvis.load_cats(lvis.get_cat_ids())

# # Print category names
# for category in categories:
#     print(category['name'])


import json

if __name__ == '__main__':
    try:
        # Path to the LVIS annotations file
        annotation_file = 'DataSetLVIsPythonFiles/lvis-api/detectable_classes/lvis_v1_image_info_test_dev.json'

        # Load the LVIS annotations
        with open(annotation_file, 'r') as f:
            lvis_data = json.load(f)

        # Extract the categories
        categories = lvis_data.get('categories', [])

        # Collect the category names
        category_names = [category['name'] for category in categories]

        # Path to the output JSON file
        output_file = 'detectable_classes.json'

        # Write the category names to the output JSON file
        with open(output_file, 'w') as f:
            json.dump(category_names, f, indent=4)

        print(f'Category names have been written to {output_file}')
    except Exception as e:
        print(f'Error: {e}')