# 概要
discord　botでサークルの入会管理を出来るようにしたbotです。
GASをAPIとして、discordもモーダルで入力した情報をスプレッドシートに書き込めるようにしています。

# 開発環境
- python 3.12.2 

- pycord 2.5.0

- docker

# GASのコード
以下のコードをデプロイして、URLを発行してください
```
const admissionSheetID = PropertiesService.getScriptProperties().getProperty('admissionSheet');
const admissionSheetName = 'シート1';
// const admissionSheet = SpreadsheetApp.openById("1115gBiiFpMXetDMDHqseg-qKYDGDTY2e2_cGCeFDTJc").getSheetByName(admissionSheetName);
const admissionSheet = SpreadsheetApp.openById(admissionSheetID).getSheetByName(admissionSheetName);

const obogSheetID = PropertiesService.getScriptProperties().getProperty('obogSheet');
const obogSheetName = 'シート1';
const obogSheet = SpreadsheetApp.openById(obogSheetID).getSheetByName(obogSheetName);

function doGet(e){
  // var data = JSON.parse(e.getData.contents);
  // var data = e.parmeter;
  var uid = e.parameters.uid;
  //列を人配列として取得
  var values = admissionSheet.getDataRange().getValues();

//  admissionSheet.appendRow([e.parameter.uid])
  var userData;

  userData = getUserData(values,uid);

   return ContentService.createTextOutput(JSON.stringify({
       'result': 'success',
       'userData': userData,
     })).setMimeType(ContentService.MimeType.JSON);

}

function doPost(e){
  var data = JSON.parse(e.postData.contents);

  var sheet = setSheet(data.sheet);

  var uid = data.uid;
  var values = sheet.getDataRange().getValues();


if(data.mode == "submit"){
  updateUserData(sheet,data,values,uid);
}else if(data.mode == "delete"){
  deleteUserData(sheet,values,uid)
}
  // admissionSheet.appendRow(data.form)


  
}
 
//uidを検索して、何列目に書いてあるか検索
 function serchUid(values,uid){
  var ans;
  for(var i = 0;i<values.length;i++){
    if(values[i][0] == uid){
      ans = i;
      break;
    }
      ans = null;
  }
  return ans;
 }

//入力ずみのユーザーデータを配列で返す関数
 function getUserData(values,uid){
  var userData;
  rowNum = serchUid(values,uid);
  userData={
          name: values[rowNum][2],
          hiragana: values[rowNum][3],
          nickname: values[rowNum][4],
          admission_year: values[rowNum][5],
          student_id: values[rowNum][6],
          rainbow_id: values[rowNum][7],
          faculty: values[rowNum][8],
          department: values[rowNum][9],
          phone: values[rowNum][10],
          gmail: values[rowNum][11]
  }

  return userData;

 }

//スプレッドシートの内容を上書きする関数
function updateUserData(sheet,data,values,uid){
  var uidRowNum = serchUid(values,uid);

  if(uidRowNum != null){
    var updateValues = [data.uid,
                              data.currentTime,
                              data.name,
                              data.hiragana,
                              data.nickname,
                              data.admission_year,
                              data.student_id,
                              data.rainbow_id,
                              data.faculty,
                              data.department,
                              data.phone,
                              data.gmail];
    //getDataRangeにしないように,[[]]にする必要あり
    sheet.getRange(uidRowNum+1,1,1,12).setValues([updateValues]);

  }else{

    sheet.appendRow([data.uid,
                              data.currentTime,
                              data.name,
                              data.hiragana,
                              data.nickname,
                              data.admission_year,
                              data.student_id,
                              data.rainbow_id,
                              data.faculty,
                              data.department,
                              data.phone,
                              data.gmail]);
  }
}

//sheetを選択するための関数
function setSheet(sheet){
  var setSheet;
  if(sheet == "admissionSheet"){
    setSheet = admissionSheet
  }else if(sheet == "obogSheet"){
    setSheet = obogSheet
  }
  // if(form == "入会届"){
  //   sheet = admissionSheet;
  // }else if(form == "OBOG届"){
  //   sheet = obogSheet;
  // }else if(form == "情報変更届"){
  //   if(role == "サークル会員"){
  //     sheet = admissionSheet;
  //   }else if (role == "OBOG"){
  //     sheet = obogSheet;
  //   }
  // }

  return setSheet;
}

//退会届を実行するための関数
function deleteUserData(sheet,values,uid){
  var uidRowNum = serchUid(values,uid);

  sheet.deleteRow(uidRowNum+1);

}

function debug(){
  var uid = "487635087954018304";
  var values = admissionSheet.getDataRange().getValues();
  var uidRowNum = serchUid(values,uid);

  admissionSheet.deleteRow(uidRowNum);
}
```


# envファイルの中身
```
TOKEN = "your_discordbot_token"

URL = "gas_url"

CIRCLE_MEMBER_ROLE_ID = "circle_member_role_id"

OBOG_ROLE_ID= "obog_role_id"
```


# 起動方法
ターミナルで以下のコマンドを打ち込む

イメージを作成
```
docker-compose build
```

コンテナを作成、起動

```
docker-compose up
```
