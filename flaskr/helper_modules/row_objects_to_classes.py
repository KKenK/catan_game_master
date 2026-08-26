def row_objects_to_classes(class_to_be_instantiated, row_objects):
    return [class_to_be_instantiated(row_object) for row_object in row_objects]
