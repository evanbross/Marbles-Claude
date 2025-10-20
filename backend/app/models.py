# Database models and utility functions

class Marble:
    def __init__(self, id=None, name=None, artist_id=None, style_id=None, 
                 size_mm=None, price=None, purchase_date=None, vendor_id=None,
                 description=None, image_url=None, ai_identified_style=None,
                 ai_confidence=None):
        self.id = id
        self.name = name
        self.artist_id = artist_id
        self.style_id = style_id
        self.size_mm = size_mm
        self.price = price
        self.purchase_date = purchase_date
        self.vendor_id = vendor_id
        self.description = description
        self.image_url = image_url
        self.ai_identified_style = ai_identified_style
        self.ai_confidence = ai_confidence
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist_id': self.artist_id,
            'style_id': self.style_id,
            'size_mm': self.size_mm,
            'price': self.price,
            'purchase_date': str(self.purchase_date) if self.purchase_date else None,
            'vendor_id': self.vendor_id,
            'description': self.description,
            'image_url': self.image_url,
            'ai_identified_style': self.ai_identified_style,
            'ai_confidence': self.ai_confidence
        }

class Artist:
    def __init__(self, id=None, name=None, bio=None, website=None):
        self.id = id
        self.name = name
        self.bio = bio
        self.website = website
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'bio': self.bio,
            'website': self.website
        }
