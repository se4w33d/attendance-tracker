from flask import Flask, render_template
from grabcode import get_attendance_code
import requests

TRAINEES = [
    "CHANEL KOH XUE MEI",
    "CHRISTINE MARLINA",
    "TAN KOK HOW",
    "CHAW FOONG LEAN",
    "VENKATESH SIDDENALLI OBANAIK",
    "CHONG WEI SHENG",
    "KWA CHEONG HONG",
    "SOON YI XIANG, ANDREW",
    "ANGELIN TANIUS",
    "KELLY KWEK FU LIANG",
    "YAO SIYUE",
    "NIDHI ATUL MISTRY",
    "CHAI SHU YING",
    "ALISON WONG CHIONG CHING",
    "GAN BENG HUAT ALVIN",
    "LIM WEIKANG, DERIC",
    "NUR ATIQAH BINTE MOHAMED AZMAN",
    "CHUA SOK CHING",
    "TAY KIT HUAT",
    "ONG KOK GUAN",
    "ANG YILIN",
    "CARLA TJANDRA",
    "PNG SEOW HUI",
    "LEE XUAN YING, SARA",
    "KWEE LANNY KURNIANINGRUM",
    "LEE SI ZHENG",
    "LI GUANGYIN",
    "KONG WAI CHONG",
    "LAW TE HAO",
    "KOH KHIA HUI, REGINA",
    "LOK SIEW WEI",
    "MUHAMED FIRDAUS BIN MOHAMED JAINI",
    "JAVEN LIM JIA HAO",
    "TAN NGAM TECK",
    "SYLVESTER NG AIK TONG",
    "JOCELYN HO KANGLI",
]

NUMBER_OF_TRAINEES = len(TRAINEES)

course_run_code = "RA341878"

url = f'https://www.myskillsfuture.gov.sg/api/take-attendance/{course_run_code}'

code_result = get_attendance_code(url) # to get attendanceCode and motCode for the API query

parameters = {
    "attendanceCode": code_result[0],
    "motCode": code_result[1]
}


app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    response = requests.get(
        "https://www.myskillsfuture.gov.sg/api/get-attendance", params=parameters
    )

    res = response.json()

    # print(json.dumps(res, sort_keys=True, indent=4))
    # print(response.status_code)

    # extract the trainee's name from the response
    trainee_attendance = [trainee['name'] for trainee in res]
   
    trainees_status = {}
    for trainee in TRAINEES:
        if trainee in trainee_attendance:
            trainees_status[trainee] = 'signed'
        else:
            trainees_status[trainee] = 'not signed'

    res1 = dict(list(trainees_status.items())[:len(trainees_status)//2]) 
    res2 = dict(list(trainees_status.items())[len(trainees_status)//2:])

    print(trainees_status)
    return render_template("index.html", status1=res1, status2=res2)

