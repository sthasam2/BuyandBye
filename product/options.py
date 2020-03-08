""" Options tuple file ('',''), """

from datetime import date

current_date = date.today()
YEARS = [
    x for x in range(1920, current_date.year + 1)
]

ITEM_CONTRACT_CHOICES = (
    ('Sale', 'Sale'),
    ('Rent', 'Rent'),
    ('Exchange', 'Exchange'),
    ('Sale/Exchange', 'Sale / Exchange',)
)

CONDITION_CHOICES = (
    ('Brand New', 'Brand New'),
    ('Used (Like New)', 'Used (Like New)'),
    ('Used (Worn Out)', 'Used (Worn Out)'),
    ('Defective', 'Defective'),
)


CATEGORY_CHOICES = (
    ('Apparel and Accessories', 'Apparel and Accessories'),
    ('Automobiles', 'Automobiles'),
    ('Beauty and Health', 'Beauty and Health'),
    ('Books', 'Books'),
    ('Business and Industry', 'Business and Industry'),
    ('Computers and Peripherals', 'Computers and Peripherals'),
    ('Electronics', 'Electronics'),
    ('Events and Happenings', 'Events and Happenings'),
    ('Home, Furnishing and Appliances', 'Home, Furnishing and Appliances'),
    ('Jobs', 'Jobs'),
    ('Mobiles and Accessories', 'Mobiles and Accesories'),
    ('Music Instruments', 'Music Instruments'),
    ('Pet and PetCare', 'Pet and Pet Care'),
    ('Real Estate', 'Real Estate'),
    ('Sports and Fitness', 'Sports and Fitness'),
    ('Services', 'Services'),
    ('Toys and Video Games', 'Toys and Video Games'),
    ('Torism and Tours', 'Tourism and Tours'),
    ('Others', 'Others'),
)

SUB_CATEGORY_CHOICES = (
    ('**Apparel and Accessories', '**Apparel and Accessories'),
    ('Children-Clothing', 'Children Clothing'),
    ('Children-Accessories', 'Children Accessories'),
    ('Bags-Luggage', 'Bags and Luggage'),
    ('Jwellery', 'Jwellery'),
    ('Mens-Clothing', 'Mens Clothing'),
    ('Mens-Accessories', 'Mens Accessories'),
    ('Mens-Shoes', 'Mens Shoes'),
    ('Sunglasses', 'Sunglasses'),
    ('Watches', 'Watches'),
    ('Womens-Clothing', 'Womens Clothing'),
    ('Womens-Accessories', 'Womens Accessories'),
    ('Womens-Shoes', 'Womens Shoes'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Automobiles', '**Automobiles'),
    ('Bicycle', 'Bicycle'),
    ('Bicycle-Parts-Accessories', 'Bicycle: Parts and Accessories'),
    ('Cars', 'Cars'),
    ('Car-Parts-Accessories', 'Car: Parts and Accessories'),
    ('Motorcycle', 'Motorcycle'),
    ('Motorcycle-Parts-Accessories', 'Motorcycle: Parts and Accessories'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Beauty & Health', 'Beauty and Health'),
    ('Bath-Toiletries', 'Bath Toiletries'),
    ('BodyCare', ' Body Care'),
    ('Cosmetics-Skin Care', 'Cosmetics & Skin Care'),
    ('Electronic-Cigarette-Vape', 'Electronic Cigarette & Vape'),
    ('Eye-Care', 'Eye Care'),
    ('Face-Care', 'Face Care'),
    ('Medical-Health-Devices', 'Medical & Health Devices'),
    ('Men-Grooming-Tools', 'Men Grooming Tools'),
    ('Perfumes-Fragrances', 'Perfumes & Fragrances'),
    ('Tattoo-Equipment', 'Tattoo Equipment'),
    ('Women-Grooming-Tools', 'Women Grooming Tools'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Books', '**Books'),

    ('Action-and-adventure', 'Action and adventure'),
    ('Alternate-history', 'Alternate history'),
    ('Anthology', 'Anthology'),
    ('Chick-lit', 'Chick-lit'),
    ('Childrens', 'Childrens'),
    ('Comic-book', 'Comic book'),
    ('Coming-of-age', 'Coming of age'),
    ('Crime', 'Crime'),
    ('Drama', 'Drama'),
    ('Fairytale', 'Fairytale'),
    ('Fantasy', 'Fantasy'),
    ('Graphic-novel', 'Graphic-novel'),
    ('Historical-fiction', 'Historical fiction'),
    ('Horror', 'Horror'), ('Mystery', 'Mystery'),
    ('Paranormal-romance', 'Paranormal romance'),
    ('Picture-book', 'Picture book'),
    ('Poetry-Review', 'Poetry Review'),
    ('Political-thriller', 'Political thriller'),
    ('Romance', 'Romance'),
    ('Satire', 'Satire'),
    ('Science-fiction', 'Science-fiction'),
    ('Short-story', 'Short story'),
    ('Suspense', 'Suspense'),
    ('Thriller', 'Thriller'),
    ('Young', 'Young'),


    ('Art', 'Art'),
    ('Autobiography', 'Autobiography'),
    ('Biography', 'Biography'),
    ('Book-review', 'Book-review'),
    ('Cookbook', 'Cookbook'),
    ('Diary', 'Diary'),
    ('Dictionary', 'Dictionary'),
    ('Encyclopedia', 'Encyclopedia'),
    ('Guide', 'Guide'),
    ('Health', 'Health'),
    ('History', 'History'),
    ('Journal', 'Journal'),
    ('Math', 'Math'),
    ('Memoir', 'Memoir'),
    ('Prayer', 'Prayer'),
    ('Religion-spirituality-new-age', 'Religion, spirituality, and new age'),
    ('Textbook', 'Textbook'),
    ('Review', 'Review'),
    ('Science', 'Science'),
    ('Self-help', 'Self-help'),
    ('Travel', 'Travel'),
    ('True-crime', 'True crime'),

    ('---------', '---------'),
    ('**Business & Industry', '**Business & Industry'),
    ('Business', 'Business'),
    ('Dealership', 'Dealership'),
    ('Equipments', 'Equipments'),
    ('Machinery', 'Machinery'),
    ('Office', 'Office'),
    ('Raw', 'Raw'),
    ('Security', 'Security'),
    ('Wholesale', 'Wholesale'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Computers-Peripherals', 'Computers and Peripherals'),
    ('Desktop', '**Desktop'),
    ('Desktop-Accessories', 'Desktop Accessories'),
    ('Games', 'Games'),
    ('Graphic-Cards', 'Graphic Cards'),
    ('Laptop', 'Laptop'),
    ('Laptop-Accessories', 'Laptop Accessories'),
    ('Monitors', 'Monitors'),
    ('Networking-Equipments', 'Networking Equipments'),
    ('Printers-Scanners', 'Printers & Scanners'),
    ('Software', 'Software'),
    ('Storage-Memory', 'Storage & Memory'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Electronics', '**Electronics'),
    ('Camera-Accessories', 'Camera Accessories'),
    ('Camcorder', 'Camcorder'),
    ('Cinema-Camera', 'Cinema Camera'),
    ('Digital-Camera', 'Digital Camera'),
    ('DIY-Hobby-Electronics', 'DIY & Hobby Electronics'),
    ('Drones', 'Drones'),
    ('DSLR-Camera', 'DSLR Camera'),
    ('Home-Theatre', 'Home Theatre'),
    ('Headphone-Earphone', 'Headphone & Earphone'),
    ('Mirror-LessCamera', 'Mirror Less Camera'),
    ('MP3-Players', 'MP3 Players'),
    ('Projectors', 'Projectors'),
    ('Speakers', 'Speakers'),
    ('Television', 'Television'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Events and Happenings', '**Events and Happenings'),
    ('Comic-Con-Tickets', 'Comic Con Tickets'),
    ('Concert-Tickets', 'Concert Tickets'),
    ('Event-Tickets', 'Event Tickets'),
    ('Movie-Tickets', 'Movie Tickets'),
    ('Sport-Tickets', 'Sport Tickets'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Furnitures', '**Furnitures'),
    ('Antique-Collectables', 'Antique & Collectables'),
    ('Art-Handicrafts', 'Art & Handicrafts'),
    ('Bath-Plumbing', 'Bath&Plumbing'),
    ('Construction-Materials', 'Construction Materials'),
    ('Decors-Interiors', 'Decors & Interiors'),
    ('Food-Drinks', 'Food & Drinks'),
    ('Garden-Outdoor', 'Garden & Outdoor'),
    ('Home-Appliances', 'Home Appliances'),
    ('Inverter-Generators', 'Inverter & Generators'),
    ('Kitchen-Appliances', 'Kitchen Appliances'),
    ('Kitchenware-Utensils', 'Kitchenware & Utensils'),
    ('Lighting-SolarElectricals', 'Lighting & Solar Electricals'),
    ('Linenes-Mattresses', 'Linenes & Mattresses'),
    ('Paint-WallPapers', 'Paint & WallPapers'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Jobs', '**Jobs'),
    ('Agriculte', 'Agriculture'),
    ('Business', 'Business'),
    ('Construction', 'Construction'),
    ('Theatre', 'Theatre'),
    ('Culinary-Cuisine', 'Culinary & Cuisine'),
    ('Labor', 'Labor'),
    ('Law', 'Law'),
    ('Marketing', 'Marketing'),
    ('IT', 'IT'),
    ('Service', 'Service'),
    ('Tourism', 'Tourism'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Mobiles-Accessories', '**Mobiles and Accesories'),
    ('Mobiles', 'Mobiles'),
    ('Accessories', 'Accessories'),
    ('Tablets', 'Tablets'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Music Instruments', '**Music Instruments'),
    ('Music-Instruments', 'Music Instruments'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Pets', '**Pets'),
    ('Pets', 'Pets'),
    ('Pets-care', 'Pets Care'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Real Estate', '**Real Estate'),
    ('Flats', 'Flats'),
    ('House', 'House'),
    ('Land', 'Land'),
    ('Rooms', 'Rooms'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Sports and Fitness', '**Sports and Fitness'),
    ('Sports-Equipments', 'Sports Equipments'),
    ('Fitness-Equipments', 'Fitness Equipments'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Services', '**Services'),
    ('Advertising-Printing-Publication', 'Advertising-Printing-Publication'),
    ('Classes-Learning-Hobby-Music', 'Classes - Learning-Hobby-Music'),
    ('Coaching-Tutors', 'Coaching & Tutors'),
    ('Computer-Sales-Repair', 'Computer - Sales & Repair'),
    ('Computer-Web-Design', 'Computer - Web &  Design'),
    ('Courses-Education-Training', 'Courses - Education & Training'),
    ('Electronics-Repair', 'Electronics Repair'),
    ('Event-Planner-Caterers', 'Event Planner & Caterers'),
    ('Financial-Legal', 'Financial & Legal'),
    ('Foreign-Education', 'Foreign Education'),
    ('Health-Fitness-Beauty', 'Health, Fitness & Beauty'),
    ('Home-Construct-Design', 'Home Construct & Design'),
    ('Home-Repair-Maintainence', 'HomeRepair & Maintainence'),
    ('Movers-Courier-Transport', 'Movers Courier & Transport'),
    ('Music-Video-Photography', 'Music-Video-Photography'),
    ('Visa-Migration', 'Visa & Migration'),
    ('Writing-Designing-Translating', 'Writing-Designing-Translating'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('**Toys-Video-Games', '**Toys and Video Games'),
    ('Arcade', 'Arcade'),
    ('Consoles', 'Consoles'),
    ('Video-Games', 'Video Games'),
    ('Toys', 'Toys'),
    ('Others', 'Others'),
    ('---------', '---------'),

    ('*Torism-Tours', '**Tourism and Tours'),
    ('International-Packages', 'International Packages'),
    ('Local-Packages', 'Local Packages'),
    ('Others', 'Others'),
    ('---------', '---------'),
)
