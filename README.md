# Hack4Change

## SereneSpace

### Theme of the Project:

To celebrate India’s G20 Presidency, the theme of the project is based upon the third sustainable development goal which is GOOD HEALTH AND WELL BEING.
SERENESPACE is designed to help users identify and manage the factors that contribute to their stress levels, with the ultimate goal of achieving a state of calm and mental stillness.

### Project Goal:

The goal of the project is to build an AI-powered chatbot that can accurately predict the stress levels of the user using machine learning algorithms. The chatbot will engage the user in a conversation and ask them questions about their daily routine and lifestyle to gather data about their stress levels. Using this data, the machine learning model will analyze the information and provide personalized suggestions and recommendations to help the user reduce their stress levels. The chatbot will aim to provide actionable insights, such as tips for mindfulness, relaxation techniques, and ways to manage work-life balance.

### Project Description:

#### Phase-1
1. Create an ML model that can accurately predict the daily stress level of the user based on their responses to a set of questions.
2. Train the model using a dataset of stress levels and corresponding data about the user's daily routine, such as work, exercise, sleep, and diet.
3. Design the model to analyze the data and provide a stress level prediction for the user.
### Phase-2
1. Create an AI chatbot that engages the user in a conversation and asks them a series of questions about their daily routine to gather data about their stress levels.
2. Chatbot will use NLP to understand the user's responses and provide personalized suggestions based.
3. Chatbot will aim to provide actionable insights and ways to manage work-life balance.

### Dataset used:

The dataset used in building the model is "Wellbeing and Lifestyle" dataset available on Kaggle.com

### Data Features:

TIMESTAMP: Date when survey was completed
FRUITS_VEGGIES: How many fruits or vegetable do you eat everyday?
DAILY_STRESS: How much stress do you typically experience everyday?
PLACES_VISITED: How many new places do you visit?
CORE_CIRCLE: How many people are very close to you?
SUPPORTING_OTHERS: How many people do you help achieve a better life?
SOCIAL_NETWORK: With how many people do you interact with during a typical day?
ACHIEVEMENT: How many remarkable achievements are you proud of?
DONATION: How many times do you donate your time or money to good causes?
BMI_RANGE: What is your body mass index (BMI) range?
TODO_COMPLETED: How well do you complete your weekly to-do lists?
FLOW: In a typical day, how many hours do you experience "FLOW"?
DAILY_STEPS: How many steps (in thousands) do you typically walk everyday?
LIVE_VISION: For how may years ahead is your life vision very clear for?
SLEEP_HOURS: About how long do you typically sleep?
LOST_VACATION: How many days of vacation do you typically lose every year?
DAILY_SHOUTING: How often do you shout or sulk at somebody?
SUFFICIENT_INCREASE: How sufficient is your increase to cover basic life expenses?
PERSONAL_AWARDS: How many recognitions have you received in your life?
TIME_FOR_PASSION: How many hours do you spend everyday doing what you are passionate about?
WEEKLY_MEDITATION: In a typical week, how many times do you have the opportunity to think about yourself?
AGE: Age groups
GENDER: Male or Female
WORK_LIFE_BALANCE: Score calculated by AH.COM algorithm and reported to user in the first report.

### Target Variable:

DAILY_STRESS is the target variable. It contains 6 classes from range 0 to 5 indicating the level and severity of stress of the user.

### Building Backend Using Flask:

Flask is a python web framework used to build lightweight, scalable webhook service; and therefore, we used it to communicate with our chatbot. When the chatbot gets the input from the user, it communicates to the machine learning model using Flask to make a prediction.

### Building Frontend Using Dialogflow:

1. Intent agent was created.
2. Intents were created.
3. Fulfillments were specified.
4. Chatbot was integrated with the backend.

### SERENE - The Chatbot:

The result of the above processes was SERENE, an AI chatbot that uses machine learning algorithms to predict the daily stress level of the user. The chatbot engages the user in conversation and asks them a series of questions about their daily routine, such as work, exercise, sleep, and diet. The chatbot provides personalized recommendations and strategies for reducing stress, such as taking breaks, practicing mindfulness, or doing breathing exercises.
 
 ### Team Details:
 
Team Name: Ode to Code

Team Members:

1. Advika Thakur- 1st Year, B.Tech AI-ML, IGDTUW (Email: adici2403@gmail.com, GitHub: https://github.com/A-dvika)
2. Ayushi Dubey- 1st Year, B.Tech AI-ML, IGDTUW (Email: adayushi232@gmail.com, GitHub: https://github.com/dubeyayushi)
3. Monya Mehta- 1st Year, B.Tech AI-ML, IGDTUW (Email: monyamehta2107@gmail.com, GitHub: https://github.com/monya217)
4. Manasvi Jindal- 1st Year, B.Tech AI-ML, IGDTUW (Email: manasvijindal28@gmail.com, GitHub: https://github.com/manasvijindal)
