#import required libraries
import numpy as np
from flask import Flask, request, make_response,render_template,jsonify
import json
import pickle
from flask_cors import cross_origin

#instantiate flask

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query = (json_)
     prediction = model.predict(query)
     return jsonify({'prediction': list(prediction)})


# geting and sending response to dialogflow
@app.route('/webhook/', methods=['GET','POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    print("req")
    res = mlprediction(req)
    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def mlprediction(req):
#sessionID=req.get('responseId')
    result = req.get("queryResult")
    #print(result)
    parameters = result.get("parameters")
    FRUITS_VEGGIES=parameters.get("FRUITS_VEGGIES")
    PLACES_VISITED = parameters.get("PLACES_VISITED")
    CORE_CIRCLE=parameters.get("CORE_CIRCLE")
    SUPPORTING_OTHERS=parameters.get("SUPPORTING_OTHERS")
    SOCIAL_NETWORK=parameters.get("SOCIAL_NETWORK")
    ACHIEVEMENT=parameters.get("ACHIEVEMENT")
    DONATION=parameters.get("DONATION")
    BMI_RANGE=parameters.get("BMI_RANGE")
    TODO_COMPLETED=parameters.get("TODO_COMPLETED")
    FLOW=parameters.get("FLOW")
    DAILY_STEPS=parameters.get("DAILY_STEPS")
    LIVE_VISION=parameters.get("LIVE_VISION")
    SLEEP_HOURS=parameters.get("SLEEP_HOURS")
    LOST_VACATION=parameters.get("LOST_VACATION")
    DAILY_SHOUTING=parameters.get("DAILY_SHOUTING")
    SUFFICIENT_INCOME=parameters.get("SUFFICIENT_INCOME")
    PERSONAL_AWARDS=parameters.get("PERSONAL_AWARDS")
    TIME_FOR_PASSION=parameters.get("TIME_FOR_PASSION")
    WEEKLY_MEDITATION=parameters.get("WEEKLY_MEDITATION")
    GENDER=parameters.get("GENDER")
    WORK_LIFE_BALANCE_SCORE=parameters.get("WORK_LIFE_BALANCE_SCORE")

    #for i in range(0,6):
    #     if (FRUITS_VEGGIES==i):
    #          FRUITS_VEGGIES = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #     if (PLACES_VISITED==i):
    #          PLACES_VISITED = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #     if (CORE_CIRCLE==i):
    #          CORE_CIRCLE = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #     if (SUPPORTING_OTHERS==i):
    #          SUPPORTING_OTHERS = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #     if (SOCIAL_NETWORK==i):
    #          SOCIAL_NETWORK = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #     if (ACHIEVEMENT==i):
    #          ACHIEVEMENT = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,6):
    #     if (DONATION==i):
    #          DONATION = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in [1,2]:
    #     if (BMI_RANGE==i):
    #          BMI_RANGE = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
#
    #for i in range(0,11):
    #     if (TODO_COMPLETED==i):
    #          TODO_COMPLETED = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #     if (FLOW==i):
    #          FLOW = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #     if (DAILY_STEPS==i):
    #          DAILY_STEPS = int(i)
    #          break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
#
    #for i in range(0,11):
    #    if (SLEEP_HOURS==i):
    #        SLEEP_HOURS = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
#
    #for i in range(0,11):
    #    if (LOST_VACATION==i):
    #        LOST_VACATION = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
#
    #for i in range(0,11):
    #    if (DAILY_SHOUTING==i):
    #        DAILY_SHOUTING = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in [1,2]:
    #    if (SUFFICIENT_INCOME==i):
    #        SUFFICIENT_INCOME = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #    if (PERSONAL_AWARDS==i):
    #        PERSONAL_AWARDS = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #    if (TIME_FOR_PASSION==i):
    #        TIME_FOR_PASSION = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in range(0,11):
    #    if (WEEKLY_MEDITATION==i):
    #        WEEKLY_MEDITATION = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in [1,2]:
    #    if (GENDER==i):
    #        GENDER = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #for i in (400, 800):
    #    if (WORK_LIFE_BALANCE_SCORE==i):
    #        WORK_LIFE_BALANCE_SCORE = int(i)
    #        break
    #else:
    #    return {
    #        "fulfillmentText": "Error please start again and enter the correct information"
    #    }
    #
    #try:
    #    int_features = [FRUITS_VEGGIES, PLACES_VISITED, CORE_CIRCLE, SUPPORTING_OTHERS, SOCIAL_NETWORK, ACHIEVEMENT, DONATION, BMI_RANGE, TODO_COMPLETED, FLOW, DAILY_STEPS, LIVE_VISION, SLEEP_HOURS, LOST_VACATION, DAILY_SHOUTING, SUFFICIENT_INCOME, PERSONAL_AWARDS, TIME_FOR_PASSION, WEEKLY_MEDITATION, GENDER, WORK_LIFE_BALANCE_SCORE]
    #    final_features = [np.array(int_features)]
#
    #except ValueError:
    #    return {
    #        "fulfillmentText": "Incorrect information supplied"
    #    }
    #print(final_features)
    #intent = result.get("intent").get('displayName')
#
    #if (intent=='Default Welcome Intent - custom - yes'):
    #    prediction = model.predict(final_features)
    #    print(prediction)
    #    if(prediction==0):
    #        status = 'Congratulations on maintaining a stress-free lifestyle! It\'s great to hear that you\'re not experiencing any stress at the moment. Keep up the good work! If you ever need support in managing stress in the future, feel free to come back and chat with us. We\'re here to help.🥳'
    #    elif(prediction==1):
    #        status = 'That\'s great to hear that you\'re experiencing very low levels of stress! It\'s important to maintain this positive mindset. Keep up the good work! In order to keep your stress levels low, consider engaging in some stress-relieving activities such as exercise, spending time with loved ones, or practicing mindfulness. These activities can help you stay calm and relaxed. If you ever need support in managing stress in the future, feel free to come back and chat with us. We\'re here to help.😁'
    #    elif(prediction==2):
    #        status = "It looks like you're experiencing mild levels of stress. Don't worry, we're here to help! Some things you can try to reduce your stress levels include taking regular breaks throughout the day to engage in relaxing activities like deep breathing, stretching, or taking a walk. Additionally, practicing mindfulness techniques like meditation or journaling can also help reduce stress. Remember, it's important to take care of yourself and prioritize your well-being. If you need any additional support, don't hesitate to reach out to a healthcare professional or come back and chat with us anytime.😀"
    #    elif(prediction==3):
    #        status = "It looks like you're experiencing moderate levels of stress. We're here to help you manage it! Some effective stress management techniques you can try include setting aside time each day to engage in relaxing activities, like exercise or spending time with friends and family. You may also find it helpful to practice mindfulness techniques like meditation or deep breathing. Remember, it's important to take care of yourself and prioritize your well-being. If you find that your stress levels are becoming unmanageable, it may be helpful to speak to a healthcare professional for additional support. In the meantime, we're here to support you however we can.🙂"
    #    elif(prediction==4):
    #        status = "It looks like you're experiencing high levels of stress. We're here to help you manage it! In order to reduce your stress levels, it's important to take immediate action. Some effective stress management techniques you can try include deep breathing exercises, progressive muscle relaxation, or talking to a friend or family member for support. Additionally, it may be helpful to speak to a healthcare professional or therapist as soon as possible to get additional support. Remember, your well-being is our top priority. If you need immediate support, please reach out to a crisis hotline or emergency services. We're here to support you in any way we can.🫂"
    #    else:
    #        status = "It looks like you're experiencing extremely high levels of stress. We're here to help you manage it! It's important that you take immediate action to address your stress levels. Some effective stress management techniques you can try include deep breathing exercises, progressive muscle relaxation, or mindfulness meditation. However, we strongly recommend that you seek professional help as soon as possible. Consider speaking with a healthcare professional, therapist, or contacting a crisis hotline for additional support. You may also want to take some time off work or other obligations to focus on your well-being. Remember, your health and well-being is our top priority. If you need immediate support, please reach out to emergency services or a crisis hotline. We're here to support you in any way we can.❤️"
    #    
    #    fulfillmentText= status
#
    #    print(fulfillmentText)
    #    print(prediction)
    return {
        "fulfillmentText": "working"
    }

if __name__ == '__main__':
    app.run(debug=True)
