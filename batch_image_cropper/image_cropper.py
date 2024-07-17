# Batch Image Cropper Class

import numpy
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter

class image_cropper:
    def __init__(self):
        self.red_sample_list = list()
        self.green_sample_list = list()
        self.blue_sample_list = list()

    # Clear RGB sample lists
    def clear_sample_lists(self):
        self.red_sample_list.clear()
        self.green_sample_list.clear()
        self.blue_sample_list.clear()

    # Find right document edge
    def find_right_edge(self, image_array):
        right_edge_list = list()
        final_edge_list_1 = list()
        final_edge_list_2 = list()
        image_height = len(image_array[0])
        image_width = len(image_array)
        for row in range(0, image_height):
            first_white_cell = True
            for col in range(0, image_width):       # 1, image_width
                cell = int(image_array[col, row])   # col, row - 1
                if cell == 1:
                    white_cell_count = +1
                    if white_cell_count > 1:
                        first_white_cell = False
                if cell == 1 and first_white_cell == True:
                    right_edge_list.append(col)
                    break
        if len(right_edge_list) != 0:
            median = numpy.mean(right_edge_list)
            standard_deviation = numpy.std(right_edge_list)
            for edge in right_edge_list:
                if edge > median - (2 * standard_deviation): final_edge_list_1.append(edge)         # Eliminate lower end outliers
            for edge in final_edge_list_1:
                if edge < median + (2 * standard_deviation): final_edge_list_2.append(edge)         # Eliminate higher end outliers
            right_edge_list = final_edge_list_2
            if len(right_edge_list) != 0: right_edge = int(numpy.quantile(right_edge_list, 0.50))   # Pick 0.5 quantile among probable right edges
            else: right_edge = 0
        else:
            right_edge = 0
        return right_edge

    # Find left document edge
    def find_left_edge(self, image_array):
        left_edge_list = list()
        final_edge_list_1 = list()
        final_edge_list_2 = list()
        image_height = len(image_array[0])
        image_width = len(image_array)              # len(image_array) - 2; len(image_array) - 1
        for row in range(0, image_height):
            first_white_cell = True
            for col in range(image_width - 1, 0, -1):
                cell = int(image_array[col, row])   # col, row - 1
                if cell == 1:
                    white_cell_count = +1
                    if white_cell_count > 1:
                        first_white_cell = False
                if cell == 1 and first_white_cell == True:
                    left_edge_list.append(col)
                    break
        if len(left_edge_list) != 0:
            median = numpy.mean(left_edge_list)
            standard_deviation = numpy.std(left_edge_list)
            for edge in left_edge_list:
                if edge > median - (2 * standard_deviation): final_edge_list_1.append(edge)     # Eliminate lower end outliers
            for edge in final_edge_list_1:
                if edge < median + (2 * standard_deviation): final_edge_list_2.append(edge)     # Eliminate higher end outliers
            left_edge_list = final_edge_list_2
            if len(left_edge_list) != 0: left_edge = int(numpy.quantile(left_edge_list, 0.50))  # Pick 0.5 quantile among probable left edges
            else: left_edge = image_width - 1   # image_width + 1; image_width
        else:
            left_edge = image_width - 1         # image_width + 1; image_width
        return left_edge

    # Find top document edge
    def find_top_edge(self, image_array):
        top_edge_list = list()
        final_edge_list_1 = list()
        final_edge_list_2 = list()
        image_height = len(image_array[0])
        image_width = len(image_array)
        for col in range(0, image_width):
            first_white_cell = True
            for row in range(0, image_height):      # 1, image_height
                cell = int(image_array[col, row])   # col - 1, row
                if cell == 1:
                    white_cell_count = +1
                    if white_cell_count > 1:
                        first_white_cell = False
                if cell == 1 and first_white_cell == True:
                    top_edge_list.append(row)
                    break
        if len(top_edge_list) != 0:
            median = numpy.mean(top_edge_list)
            standard_deviation = numpy.std(top_edge_list)
            for edge in top_edge_list:
                if edge > median - (2 * standard_deviation): final_edge_list_1.append(edge)     # Eliminate lower end outliers
            for edge in final_edge_list_1:
                if edge < median + (2 * standard_deviation): final_edge_list_2.append(edge)     # Eliminate higher end outliers
            top_edge_list = final_edge_list_2
            if len(top_edge_list) != 0: top_edge = int(numpy.quantile(top_edge_list, 0.50))     # Pick 0.5 quantile among probable top edges
            else: top_edge = 0
        else:
            top_edge = 0
        return top_edge

    # Find buttom document edge
    def find_buttom_edge(self, image_array):
        buttom_edge_list = list()
        final_edge_list_1 = list()
        final_edge_list_2 = list()
        image_height = len(image_array[0])          # len(image_array[0]) - 2; len(image_array[0]) - 1
        image_width = len(image_array)
        for col in range(0, image_width):
            first_white_cell = True
            for row in range(image_height - 1, 0, -1):
                cell = int(image_array[col, row])   # col - 1, row
                if cell == 1:
                    white_cell_count = +1
                    if white_cell_count > 1:
                        first_white_cell = False
                if cell == 1 and first_white_cell == True:
                    buttom_edge_list.append(row)
                    break
        if len(buttom_edge_list) != 0:
            median = numpy.mean(buttom_edge_list)
            standard_deviation = numpy.std(buttom_edge_list)
            for edge in buttom_edge_list:
                if edge > median - (2 * standard_deviation): final_edge_list_1.append(edge)             # Eliminate lower end outliers
            for edge in final_edge_list_1:
                if edge < median + (2 * standard_deviation): final_edge_list_2.append(edge)             # Eliminate higher end outliers
            buttom_edge_list = final_edge_list_2
            if len(buttom_edge_list) != 0: buttom_edge = int(numpy.quantile(buttom_edge_list, 0.50))    # Pick 0.5 quantile among probable buttom edges
            else: buttom_edge = image_height - 1    # image_height + 1; image_height
        else:
            buttom_edge = image_height - 1          # image_height + 1; image_height
        return buttom_edge

    # Crop image object
    def crop(self, original_image):
        # Convert original image object to 3D array
        original_image_array = numpy.array(original_image)

        # If original image is in horizontal position, rotate to vertical position and overwrite image object
        image_height = len(original_image_array[0])
        image_width = len(original_image_array)
        if image_width < image_height:  # <=
            original_image_array = numpy.rot90(original_image_array)
            original_image = Image.fromarray(original_image_array)
        else:
            pass

        # Make temporary copy of original image object for background removal process
        temp_image = original_image

        # Convert temp image object to 3D array
        temp_image_array = numpy.array(temp_image)

        # Take RGB samples from top, buttom, left, and right edges of image object
        image_height = len(temp_image_array[0])
        image_width = len(temp_image_array)

        self.clear_sample_lists()
        for row in range(0, image_height):
            for col in range(0, 10):
                self.red_sample_list.append(temp_image_array[col, row][0])
                self.green_sample_list.append(temp_image_array[col, row][1])
                self.blue_sample_list.append(temp_image_array[col, row][2])
        top_red_sample = int(numpy.median(self.red_sample_list))        # Pick median red sample
        top_green_sample = int(numpy.median(self.green_sample_list))    # Pick median green sample
        top_blue_sample = int(numpy.median(self.blue_sample_list))      # Pick median blue sample

        self.clear_sample_lists()
        for row in range(0, image_height):
            for col in range(image_width - 1, image_width - 11, -1):
                self.red_sample_list.append(temp_image_array[col, row][0])
                self.green_sample_list.append(temp_image_array[col, row][1])
                self.blue_sample_list.append(temp_image_array[col, row][2])
        buttom_red_sample = int(numpy.median(self.red_sample_list))     # Pick median red sample
        buttom_green_sample = int(numpy.median(self.green_sample_list)) # Pick median green sample
        buttom_blue_sample = int(numpy.median(self.blue_sample_list))   # Pick median blue sample

        self.clear_sample_lists()
        for col in range(0, image_width):
            for row in range(0, 10):
                self.red_sample_list.append(temp_image_array[col, row][0])
                self.green_sample_list.append(temp_image_array[col, row][1])
                self.blue_sample_list.append(temp_image_array[col, row][2])
        left_red_sample = int(numpy.median(self.red_sample_list))       # Pick median red sample
        left_green_sample = int(numpy.median(self.green_sample_list))   # Pick median green sample
        left_blue_sample = int(numpy.median(self.blue_sample_list))     # Pick median blue sample

        self.clear_sample_lists()
        for col in range(0, image_width):
            for row in range(image_height - 1, image_height - 11, -1):
                self.red_sample_list.append(temp_image_array[col, row][0])
                self.green_sample_list.append(temp_image_array[col, row][1])
                self.blue_sample_list.append(temp_image_array[col, row][2])
        right_red_sample = int(numpy.median(self.red_sample_list))      # Pick median red sample
        right_green_sample = int(numpy.median(self.green_sample_list))  # Pick median green sample
        right_blue_sample = int(numpy.median(self.blue_sample_list))    # Pick median blue sample

        # Calculate overall RGB sample
        red_sample = int(numpy.median([right_red_sample, left_red_sample, top_red_sample, buttom_red_sample]))              # Pick overall median red sample
        green_sample = int(numpy.median([right_green_sample, left_green_sample, top_green_sample, buttom_green_sample]))    # Pick overall median green sample
        blue_sample = int(numpy.median([right_blue_sample, left_blue_sample, top_blue_sample, buttom_blue_sample]))         # Pick overall median blue sample

        # Add dark margines to orginal and temp image objects if no background detected
        if red_sample + green_sample + blue_sample >= 675:
            original_image = ImageOps.expand(original_image, border = 100, fill=0)
            temp_image = original_image.filter(ImageFilter.SMOOTH_MORE)
            temp_image = temp_image.filter(ImageFilter.SMOOTH_MORE)
            temp_image = temp_image.filter(ImageFilter.SMOOTH_MORE)
            # print('Dark margine added.')    # For debugging only

        # Manipulate temp image object to enhance document edge detection
        temp_image = ImageOps.autocontrast(temp_image, cutoff=(20, 15), ignore=None, mask=None, preserve_tone=False)
        temp_image = temp_image.convert("1", dither = False)
        temp_image = temp_image.filter(ImageFilter.EDGE_ENHANCE)
        temp_image = temp_image.filter(ImageFilter.MinFilter(3))
        temp_image = temp_image.filter(ImageFilter.MinFilter(3))
        temp_image = temp_image.filter(ImageFilter.MinFilter(3))
        temp_image = temp_image.filter(ImageFilter.MinFilter(3))
        temp_image = temp_image.filter(ImageFilter.MinFilter(3))
        temp_image = temp_image.filter(ImageFilter.MaxFilter(3))
        temp_image = temp_image.filter(ImageFilter.MaxFilter(3))
        temp_image = temp_image.filter(ImageFilter.MaxFilter(3))
        temp_image = temp_image.filter(ImageFilter.SMOOTH_MORE)
        temp_image = temp_image.filter(ImageFilter.SMOOTH_MORE)
        temp_image = temp_image.filter(ImageFilter.SMOOTH_MORE)

        # Re-convert modified original and temp image objects to 3D arrays
        original_image_array = numpy.array(original_image)
        temp_image_array = numpy.array(temp_image)

        # Find document edges
        buttom_edge = self.find_buttom_edge(temp_image_array)
        top_edge = self.find_top_edge(temp_image_array)
        left_edge = self.find_left_edge(temp_image_array)
        right_edge = self.find_right_edge(temp_image_array)

        # Remove background
        image_height = len(temp_image_array[0])
        image_width = len(temp_image_array)
        for row in range(image_height - 1, buttom_edge, -1):
            original_image_array = numpy.delete(original_image_array, (row), axis=1)
            temp_image_array = numpy.delete(temp_image_array, (row), axis=1)
        for row in range(top_edge, 0, -1):
            original_image_array = numpy.delete(original_image_array, (row), axis=1)
            temp_image_array = numpy.delete(temp_image_array, (row), axis=1)
        for col in range(image_width - 1, left_edge, -1):
            original_image_array = numpy.delete(original_image_array, (col), axis=0)
            temp_image_array = numpy.delete(temp_image_array, (col), axis=0)
        for col in range(right_edge, 0, -1):
            original_image_array = numpy.delete(original_image_array, (col), axis=0)
            temp_image_array = numpy.delete(temp_image_array, (col), axis=0)

        # Convert cropped 3D array back to image object
        new_image = Image.fromarray(original_image_array)
        # new_image = Image.fromarray(temp_image_array)   # For debugging only

        # Make final enhancements to cropped image object
        new_image = ImageOps.expand(new_image, border = 10, fill=0)
        new_image = ImageOps.autocontrast(new_image, cutoff=(10, 15), ignore=None, mask=None, preserve_tone=False)  # Alternative: cutoff=(12.5, 20)
        new_image = ImageOps.grayscale(new_image)

        # Return cropped image object
        return new_image