const express = require('express');
const app = express();
const port = '포트번호';
const bodyParser = require('body-parser');

let a_1 = 0, b_1 = 0, c_1 = 0, d_2 = 0, e_2 = 0, f_2 = 0;
let data_h = {};
let data_s = {};
let data_room = {};
let data_text = "";
let data_comment = {};
let txt = "조용히 해주세요."

// JSON 파싱을 위한 미들웨어 등록
app.use(bodyParser.json());

// GET 요청 핸들러
app.get('/', function(req, res) {
  // GET 요청 처리 작업
  res.send("get 요청에 따라 동작합니다.");
});

// POST 요청 핸들러
app.post('/hosil', function (req, res) {
  
  if (req.body["h_sound1"] != null) {
    console.log('h_sound : ' + req.body["h_sound1"]);
    console.log('h_alert : ' + req.body["h_alert1"]);
    console.log('h_room : ' + req.body["h_room1"]);

    a_1 = req.body["h_sound1"];
    b_1 = req.body["h_alert1"];
    c_1 = req.body["h_room1"];
    data_h = {
      "comment": "정상적으로 통신중입니다."
    }
  } else {
    console.log("1호실 데이터 수신을 실패했습니다.");
    data_h = {
      "comment": "1호실 데이터 수신을 실패했습니다."
    }
  }

  if (req.body["h_sound2"] != null) {
    console.log('h_sound2 : ' + req.body["h_sound2"]);
    console.log('h_alert2 : ' + req.body["h_alert2"]);
    console.log('h_room2 : ' + req.body["h_room2"]);
    d_2 = req.body["h_sound2"];
    e_2 = req.body["h_alert2"];
    f_2 = req.body["h_room2"];
    data_h = {
      "comment": "정상적으로 통신중입니다."
    }
  } else {
    console.log("2호실 데이터 수신을 실패했습니다.");
    data_h = {
      "comment": "2호실 데이터 수신을 실패했습니다."
    }
  }

  data_room = {
    "sound_101": a_1,
    "alert_101": b_1,
    "room_101": c_1,
    "sound_102": d_2,
    "alert_102": e_2,
    "room_102": f_2
  }

  // 응답 전송
  res.send(data_h);
});

// POST 요청 핸들러
app.post('/sagam', function (req, res) {
  console.log(req.body);
  if (req.body["room"] != null) {
    data_s = data_room;
    console.log(data_s);
  } else {
    console.log("사감의 요청을 수신받지 못했습니다.");
    data_s = {
      "comment": "사감의 요청을 수신받지 못했습니다."
    }
  }

  if (req.body["warning"] != null) {
    
    data_text = req.body["warning"];
    console.log(data_text)

  } else {
    console.log("사감의 요청을 수신받지 못했습니다.");
    data_s = {
      "comment": "사감의 요청을 수신받지 못했습니다."
    }
  }

  res.send(data_s);
});

if (data_text == "1") {
  app.post('/hosil1', function (req, res) {
    if (req.body["warning_check"] != null) {
      data_comment = {
        "notion" : txt
      };
      console.log(data_comment);
    } else {
      console.log("호실1의 요청을 수신받지 못했습니다.");
      data_s = {
        "comment": "호실1의 요청을 수신받지 못했습니다."
      }
    }
    res.send(data_comment);
  });
} else if (data_text == "2") {
  app.post('/hosil2', function (req, res) {
    if (req.body["warning_check"] != null) {
      data_comment = {
        "notion" : txt
      };
      console.log(data_comment);
    } else {
      console.log("호실2의 요청을 수신받지 못했습니다.");
      data_s = {
        "comment": "호실2의 요청을 수신받지 못했습니다."
      }
    }
    res.send(data_comment);
  });
}
  
// 서버 시작
app.listen(port, () => {
  console.log(`웹 서버가 ${port}포트로 실행 중입니다.`);
});
