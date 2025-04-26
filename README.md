The AI-Powered Touchless Shopping Basket is an innovative solution designed to revolutionize the traditional shopping experience by integrating advanced 
technologies such as Artificial Intelligence (AI), Internet of Things (IoT), and Voice Recognition. 
This system aims to provide a hands-free, autonomous shopping assistant that follows customers, eliminates the need for manual cart handling, 
and supports seamless voice-based product selection and checkout. The primary goals are to enhance convenience, improve hygiene, and cater to individuals with mobility challenges.


Objective of the Project:
Autonomous Navigation: Develop a shopping basket that can follow customers throughout the store without manual intervention
Voice-Activated Operations: Implement voice recognition for adding or removing products from the basket.
Real-Time Billing: Enable automatic item detection and real-time cost calculation to streamline the checkout process.
Enhanced Hygiene: Reduce physical contact points to improve sanitary conditions.
Accessibility: Provide a shopping solution that caters to individuals with mobility impairments.


Literature Survey
The evolution of shopping carts has been a focal point in retail innovation, aiming to enhance customer experience and streamline store operations. This literature survey examines recent advancements in smart shopping cart technologies, highlighting their features, limitations, and how the proposed AI-Powered Touchless Shopping Basket addresses these challenges.
1. Autonomous Billing and Product Detection
•	Autonomous Billing Cart for Retail Store: This system integrates RFID technology to automate product scanning and billing processes, reducing checkout times and enhancing customer convenience (ieeexplore.ieee.org).
•	An Intelligent Shopping Cart with Automatic Product Detection: This prototype utilizes sensors to detect items added to the cart, displaying product information on a user interface. It also incorporates user authentication through biometric systems (ieeexplore.ieee.org).
Limitations & Proposed Solutions:
•	RFID Dependency: Reliance on RFID tags necessitates additional infrastructure. Solution: Implement computer vision techniques for product recognition.
•	User Authentication Complexity: Biometric systems introduce privacy concerns. Solution: Use voice recognition for authentication.
2. IoT Integration and Mobile Applications
•	IoT Based Smart Shopping Trolley with Mobile Cart Application: This design leverages IoT to generate bills and integrates with mobile applications, aiming to reduce queues at billing counters (ieeexplore.ieee.org).
Limitations & Proposed Solutions:
•	Mobile Dependency: Customers may not prefer using mobile apps. Solution: Incorporate an onboard display system.

3. Autonomous Navigation and User Assistance
•	Autonomous Shopping Cart: A New Concept of Service Robot: This concept introduces a cart that assists customers by following them and aiding in item transportation, particularly benefiting those with disabilities (ieeexplore.ieee.org).
Limitations & Proposed Solutions:
•	Navigation Accuracy: Ensuring precise movement in crowded environments is challenging. Solution: Implement AI-powered navigation algorithms with obstacle avoidance.
4. Industry Implementations and Consumer Acceptance
•	Smart Carts in Retail: Companies like Veeve and Caper AI have introduced smart carts equipped with features such as product recommendations and autonomous checkout (forbes.com).
Limitations & Proposed Solutions:
•	Consumer Adaptation: Customers may hesitate to adopt new technologies due to privacy concerns. Solution: Focus on intuitive interfaces and data security measures.



Proposed Methodology
The AI-Powered Touchless Shopping Basket consists of:
Self-Driving Mechanism: Basket moves autonomously, following the customer using AI-powered tracking and depth-sensing cameras.
Voice-Controlled Product Selection: Customers can simply say, "Add 1kg of apples," and the system will register the item.
Smart Billing System: Integrates RFID sensors and computer vision for automatic item detection and real-time cost calculation.
Digital Payment & Checkout: Supports voice-based checkout via mobile apps or UPI.
Anti-Theft Mechanism: Alerts the system if an unpurchased item is removed
Requirements
1. Hardware Requirements:
•	Processor: Raspberry Pi 4 / Jetson Nano
•	Sensors: LiDAR, Ultrasonic, RFID Reader
•	Camera: High-resolution for product detection
•	Microphone: For voice commands
•	Battery: Rechargeable lithium-ion
•	Motorized Wheels: For movement
•	Display Screen: LCD/OLED
2. Software Requirements:
•	OS: Raspberry Pi OS / Ubuntu
•	Languages: Python, C++
•	AI/ML: TensorFlow, OpenCV, DeepSpeech
•	Database: Firebase / MySQL
•	Web Backend: Flask / Django
•	Payment API: UPI / Razorpay




3. Functional Requirements:
•	Autonomous basket following
•	Voice-controlled item selection
•	Real-time billing & display
•	Contactless payment integration
•	Automatic checkout & reset



4. Non-Functional Requirements:
•	Low power consumption
•	Lightweight & durable
•	Fast response time (<1 sec)
•	Multi-language support
