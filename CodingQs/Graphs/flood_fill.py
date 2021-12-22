from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        # Assume m x n image
        m, n = len(image), len(image[0])
        
        # Fill pixel than recurse on neighbors
        def fill_pixel(color: int, new_color: int, pixel_x: int, pixel_y: int, x_bound:int, y_bound: int):
            if pixel_x < 0 or pixel_x >= x_bound or pixel_y < 0 or pixel_y >= y_bound:
                return
            
            pixel_color = image[pixel_x][pixel_y]
            if pixel_color == color:
                image[pixel_x][pixel_y] = new_color
            if pixel_color == new_color or pixel_color != color:
                # Exiting recurion
                return
                
            # print("Recursing Left")
            return fill_pixel(color, new_color, pixel_x-1, pixel_y, x_bound, y_bound), \
            fill_pixel(color, new_color, pixel_x+1, pixel_y, x_bound, y_bound), \
            fill_pixel(color, new_color, pixel_x, pixel_y-1, x_bound, y_bound), \
            fill_pixel(color, new_color, pixel_x, pixel_y+1, x_bound, y_bound)
            
            
        fill_pixel(color, newColor, sr, sc, m, n)
        return image