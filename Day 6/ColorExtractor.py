import colorgram
class ColorExtractor:
    def extract_colors(self,ref,num_colors):
        rgb = []
        colors = colorgram.extract(ref,num_colors)

        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            rgb_color = (r,g,b)
            rgb.append(rgb_color)

        return rgb