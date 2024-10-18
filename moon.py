# 8. Draw the moon
# Draw the moon (crescent shape in the sky)
import cairo

# Set up the canvas dimensions
WIDTH, HEIGHT = 900, 700

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Set background color (white)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set line width for the outlines
ctx.set_line_width(4)
ctx.arc(700, 100, 40, 0,2 * 3.14)
ctx.set_source_rgb(0.8, 0.8, 0.8)  # Light gray color for the moon
ctx.fill()
ctx.stroke()

# Draw the flipped crescent (facing left, simulating shadow)
ctx.arc(680, 100, 40, 0,2 * 3.14)  # Changed the center of the arc to the left
ctx.set_source_rgb(1, 1, 1)  # White color to create the crescent shadow
ctx.fill()

# Save the drawing to a PNG file
surface.write_to_png("Output.png")