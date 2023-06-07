"""
Bounding box utils
"""

import numpy as np


class Bbox:
    def __init__(self, bbox=None):
        if bbox != None:
            self.parse_bbox(bbox)

    def parse_bbox(self, bbox):
        self.bbox = bbox
        self.p1 = bbox[:2]
        self.p3 = bbox[2:]

        self.x1, self.y1 = self.p1
        self.x3, self.y3 = self.p3

        self.bbox_h = self.y3 - self.y1
        self.bbox_w = self.x3 - self.x1

    def get_rectangle_coordinates(self):
        # get rectangle coordinates
        self.rect = [
            [self.x1, self.y1],
            [self.x3, self.y1],
            [self.x3, self.y3],
            [self.x1, self.y3],
        ]
        return self.rect

    def get_bbox_centroid(self):
        xc = (self.x1 + self.x3) / 2
        yc = (self.y1 + self.y3) / 2

        return xc, yc

    def get_bbox_area(self):
        return self.bbox_h * self.bbox_w

    def norm_bbox(self, img_w, img_h):
        self.x1_norm = self.x1 / img_w
        self.y1_norm = self.y1 / img_h

        self.x3_norm = self.x3 / img_w
        self.y3_norm = self.y3 / img_h

        self.bbox_norm = [
            self.x1_norm,
            self.y1_norm,
            self.x3_norm,
            self.y3_norm,
        ]
        return self.bbox_norm

    def denorm_bbox(self, img_w, img_h):
        self.x1_denorm = self.x1 * img_w
        self.y1_denorm = self.y1 * img_h

        self.x3_denorm = self.x3 * img_w
        self.y3_denorm = self.y3 * img_h

        self.bbox_denorm = [
            self.x1_denorm,
            self.y1_denorm,
            self.x3_denorm,
            self.y3_denorm,
        ]
        return self.bbox_denorm

    @staticmethod
    def get_iou(b1, b2):
        ix_1 = max(b1[0], b2[0])
        iy_1 = max(b1[1], b2[1])

        ix_3 = min(b1[2], b2[2])
        iy_3 = min(b1[3], b2[3])

        inter_bbox = [ix_1, iy_1, ix_3, iy_3]
        inter_bbox = Bbox(inter_bbox)
        inter_area = inter_bbox.get_bbox_area()

        union_area = Bbox(b1).get_bbox_area() + Bbox(b2).get_bbox_area() - inter_area

        if union_area != 0:
            iou = round((inter_area / union_area), 8)
            return iou
        else:
            return 0

    @staticmethod
    def check_box_a_in_box_b(b1, b2):
        b1 = np.array(b1)
        b2 = np.array(b2)

        p1_in_box_b = (b1[:2] >= b2[:2]).all()
        p3_in_box_b = (b1[2:] <= b2[2:]).all()

        b1_in_b2 = p1_in_box_b and p3_in_box_b

        return b1_in_b2

    @staticmethod
    def plot_bbox(image_path, bboxes, labels, colors=None, fill=False):
        from PIL import Image
        import torch
        from torchvision.utils import draw_bounding_boxes
        from torchvision.transforms.functional import pil_to_tensor, to_pil_image

        image = Image.open(image_path)

        img = draw_bounding_boxes(
            pil_to_tensor(image),
            boxes=torch.tensor(bboxes),
            colors=colors,
            labels=labels,
            fill=fill,
        )

        return to_pil_image(img)

    # todo
    @staticmethod
    def check_bbox_in_image_bounds(self, img_h, img_w):
        pass
