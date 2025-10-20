USE marble_collection;

-- Insert common marble styles
INSERT INTO styles (name, description) VALUES
('Latticino', 'Features twisted white threads in a clear or colored base'),
('Lutz', 'Contains goldstone (copper aventurine) flakes'),
('Swirl', 'Features swirling colored bands'),
('Onionskin', 'Layered surface with stretched and folded colors'),
('Mica', 'Contains flecks of mica for sparkle'),
('End of Day', 'Made from leftover glass with multiple colors'),
('Cat\'s Eye', 'Features vanes radiating from center'),
('Clambroth', 'Opaque with a milky, mottled appearance'),
('Sulphide', 'Contains a figure encased in clear glass'),
('Contemporary Art', 'Modern artistic marbles');

-- Sample artists
INSERT INTO artists (name, bio, website) VALUES
('Unknown', 'Artist information not available', NULL),
('Handmade', 'Various handmade marble artists', NULL);

-- Sample vendors
INSERT INTO vendors (name, location) VALUES
('Local Marble Shop', 'Main Street'),
('Online Marketplace', 'Internet'),
('Marble Convention', 'Various Locations');
