let myChart1; // 첫 번째 차트 인스턴스
let myChart2; // 두 번째 차트 인스턴스

/**
 * 서버에서 보내는 Json 형식에 따른 script 
 */
// 서버에서 오는 데이터 (예시)
// const responseData = [
//     { "region": "강원", "experience": "신입", "rate": 30 },
//     { "region": "강원", "experience": "경력", "rate": 40 },
//     { "region": "강원", "experience": "경력무관", "rate": 30 },
//     { "region": "경기", "experience": "신입", "rate": 35 },
//     { "region": "경기", "experience": "경력", "rate": 40 },
//     { "region": "경기", "experience": "경력무관", "rate": 25 },
//     { "region": "경남", "experience": "신입", "rate": 40 },
//     { "region": "경남", "experience": "경력", "rate": 35 },
//     { "region": "경남", "experience": "경력무관", "rate": 25 },
//     { "region": "경북", "experience": "신입", "rate": 45 },
//     { "region": "경북", "experience": "경력", "rate": 30 },
//     { "region": "경북", "experience": "경력무관", "rate": 25 },
//     { "region": "광주", "experience": "신입", "rate": 50 },
//     { "region": "광주", "experience": "경력", "rate": 30 },
//     { "region": "광주", "experience": "경력무관", "rate": 20 },
//     { "region": "대구", "experience": "신입", "rate": 55 },
//     { "region": "대구", "experience": "경력", "rate": 30 },
//     { "region": "대구", "experience": "경력무관", "rate": 15 },
//     { "region": "대전", "experience": "신입", "rate": 40 },
//     { "region": "대전", "experience": "경력", "rate": 40 },
//     { "region": "대전", "experience": "경력무관", "rate": 20 },
//     { "region": "부산", "experience": "신입", "rate": 30 },
//     { "region": "부산", "experience": "경력", "rate": 50 },
//     { "region": "부산", "experience": "경력무관", "rate": 20 },
//     { "region": "서울", "experience": "신입", "rate": 40 },
//     { "region": "서울", "experience": "경력", "rate": 30 },
//     { "region": "서울", "experience": "경력무관", "rate": 30 },
//     { "region": "세종", "experience": "신입", "rate": 45 },
//     { "region": "세종", "experience": "경력", "rate": 30 },
//     { "region": "세종", "experience": "경력무관", "rate": 25 },
//     { "region": "울산", "experience": "신입", "rate": 50 },
//     { "region": "울산", "experience": "경력", "rate": 30 },
//     { "region": "울산", "experience": "경력무관", "rate": 20 },
//     { "region": "인천", "experience": "신입", "rate": 35 },
//     { "region": "인천", "experience": "경력", "rate": 40 },
//     { "region": "인천", "experience": "경력무관", "rate": 25 },
//     { "region": "전북", "experience": "신입", "rate": 40 },
//     { "region": "전북", "experience": "경력", "rate": 35 },
//     { "region": "전북", "experience": "경력무관", "rate": 25 },
//     { "region": "제주", "experience": "신입", "rate": 30 },
//     { "region": "제주", "experience": "경력", "rate": 40 },
//     { "region": "제주", "experience": "경력무관", "rate": 30 },
//     { "region": "충남", "experience": "신입", "rate": 50 },
//     { "region": "충남", "experience": "경력", "rate": 30 },
//     { "region": "충남", "experience": "경력무관", "rate": 20 },
//     { "region": "충북", "experience": "신입", "rate": 40 },
//     { "region": "충북", "experience": "경력", "rate": 35 },
//     { "region": "충북", "experience": "경력무관", "rate": 25 },
//     { "region": "해외", "experience": "신입", "rate": 20 },
//     { "region": "해외", "experience": "경력", "rate": 60 },
//     { "region": "해외", "experience": "경력무관", "rate": 20 },
// ]; // 더미데이터 



/**
 * @function drawChart 막대그래프 그리는 메소드 
 * @author dhshin
 * @param {*} responseData 지역별 채용공고로 신입/경력 비중 data  .json 형식
 */
function drawChart(responseData) {
    console.log(responseData)

    const labels = [...new Set(responseData.map(data => data.region))];

    const 신입비율 = labels.map(label => {
        const found = responseData.find(data => data.region === label && data.experience === "신입");
        return found ? found.rate : 0;
    });

    const 경력비율 = labels.map(label => {
        const found = responseData.find(data => data.region === label && data.experience === "경력");
        return found ? found.rate : 0;
    });

    const 경력무관비율 = labels.map(label => {
        const found = responseData.find(data => data.region === label && data.experience === "경력무관");
        return found ? found.rate : 0;
    });

    const trace1 = {
        x: labels,
        y: 신입비율,
        name: '신입 비율',
        type: 'bar',
        marker: {
            color: '#4CAF50', // Green
            line: { width: 1.5 }
        }
    };

    const trace2 = {
        x: labels,
        y: 경력비율,
        name: '경력 비율',
        type: 'bar',
        marker: {
            color: '#2196F3', // Blue
            line: { width: 1.5 }
        }
    };

    const trace3 = {
        x: labels,
        y: 경력무관비율,
        name: '경력무관 비율',
        type: 'bar',
        marker: {
            color: '#FFC107', // Amber
            line: { width: 1.5 }
        }
    };

    const data = [trace1, trace2, trace3];

    const layout = {
        title: '지역별 신입/경력 비율',
        barmode: 'group',
        xaxis: {
            title: '지역',
            showgrid: false,
            zeroline: false,
            showline: true
        },
        yaxis: {
            title: '비율 (%)',
            showgrid: true,
            zeroline: false,
            showline: true
        },
        legend: {
            orientation: 'h',
            yanchor: 'bottom',
            y: 1.02,
            xanchor: 'right',
            x: 1
        },
        paper_bgcolor: '#f4f4f4',
        plot_bgcolor: '#f4f4f4'
    };

    Plotly.newPlot('myDiv', data, layout);

}
/**
 * @function 
 * @author
 * @param {*} responseData 
 */
function drawChart2(responseData) {
    // 각 경험 유형별 데이터 생성
    const regions = [...new Set(responseData.map(data => data.region))];
    const newbieRates = regions.map(region => responseData.find(data => data.region === region && data.experience === "신입").rate);
    const experiencedRates = regions.map(region => responseData.find(data => data.region === region && data.experience === "경력").rate);
    const nonExperiencedRates = regions.map(region => responseData.find(data => data.region === region && data.experience === "경력무관").rate);

    // 꺽은선 그래프 데이터
    const trace1 = {
        x: regions,
        y: newbieRates,
        mode: 'lines+markers',
        name: '신입 비율',
        line: { shape: 'spline', width: 2, color: '#1f77b4' }
    };

    const trace2 = {
        x: regions,
        y: experiencedRates,
        mode: 'lines+markers',
        name: '경력 비율',
        line: { shape: 'spline', width: 2, color: '#ff7f0e' }
    };

    const trace3 = {
        x: regions,
        y: nonExperiencedRates,
        mode: 'lines+markers',
        name: '경력무관 비율',
        line: { shape: 'spline', width: 2, color: '#2ca02c' }
    };

    const data = [trace1, trace2, trace3];

    const layout = {
        title: '지역별 신입/경력 비율',
        xaxis: {
            title: '지역',
            tickangle: -45
        },
        yaxis: {
            title: '비율 (%)',
            showgrid: true,
            zeroline: false
        },
        legend: {
            x: 0,
            y: 1,
            bgcolor: 'rgba(255, 255, 255, 0.8)',
            bordercolor: 'black',
            borderwidth: 1
        },
        paper_bgcolor: '#f5f5f5',
        plot_bgcolor: '#f5f5f5'
    };

    // 그래프 그리기
    Plotly.newPlot('lineChart', data, layout);

}


function drawCombinedChart(responseData) {
    // 지역 라벨 생성
    const labels = [...new Set(responseData.map(data => data.region))];

    // 비율 계산
    const 신입비율 = labels.map(label => {
        const found = responseData.find(data => data.region === label && data.experience === "신입");
        return found ? found.rate : 0;
    });

    const 경력비율 = labels.map(label => {
        const found = responseData.find(data => data.region === label && data.experience === "경력");
        return found ? found.rate : 0;
    });

    const 경력무관비율 = labels.map(label => {
        const found = responseData.find(data => data.region === label && data.experience === "경력무관");
        return found ? found.rate : 0;
    });

    // 막대 그래프 데이터
    const trace1 = {
        x: labels,
        y: 신입비율,
        name: '신입 비율',
        type: 'bar',
        marker: {
            color: 'rgba(173, 216, 230, 0.5)',
            line: { width: 1.5 }
        }
    };

    const trace2 = {
        x: labels,
        y: 경력비율,
        name: '경력 비율',
        type: 'bar',
        marker: {
            color: 'rgba(174, 238, 174, 0.5)', // Light Blue
            line: { width: 1.5 }
        }
    };

    const trace3 = {
        x: labels,
        y: 경력무관비율,
        name: '경력무관 비율',
        type: 'bar',
        marker: {
            color: 'rgba(230, 230, 250, 0.5)',
            line: { width: 1.5 }
        }
    };

    // 꺽은선 그래프 데이터
    const lineTrace1 = {
        x: labels,
        y: 신입비율,
        mode: 'lines+markers',
        name: '신입 비율 (꺽은선)',
        line: { shape: 'spline', width: 3, color: '#1f77b4' } // Bold Blue
    };

    const lineTrace2 = {
        x: labels,
        y: 경력비율,
        mode: 'lines+markers',
        name: '경력 비율 (꺽은선)',
        line: { shape: 'spline', width: 3, color: '#ff7f0e' } // Bold Orange
    };

    const lineTrace3 = {
        x: labels,
        y: 경력무관비율,
        mode: 'lines+markers',
        name: '경력무관 비율 (꺽은선)',
        line: { shape: 'spline', width: 3, color: '#2ca02c' } // Bold Green
    };

    const data = [trace1, trace2, trace3, lineTrace1, lineTrace2, lineTrace3];

    const layout = {
        title: '지역별 신입/경력 비율',
        barmode: 'group',
        xaxis: {
            title: '지역',
            showgrid: false,
            zeroline: false,
            showline: true,
            tickangle: -45 // 꺽은선 그래프 x축 각도 조정
        },
        yaxis: {
            title: '비율 (%)',
            showgrid: true,
            zeroline: false,
            showline: true
        },
        legend: {
            orientation: 'h',
            yanchor: 'bottom',
            y: 1.02,
            xanchor: 'right',
            x: 1
        },
        paper_bgcolor: '#f4f4f4',
        plot_bgcolor: '#f4f4f4'
    };

    // 그래프 그리기
    Plotly.newPlot('myDiv2', data, layout);
}



// CSRF 토큰을 Django 템플릿에서 가져오기
const csrftoken = "{{ csrf_token }}";