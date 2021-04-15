import React, {useState, useEffect} from 'react'
import { Chart } from 'react-charts'
import axios from "axios"


export default function Bartchat() {
    const [newData, setNewData] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
          const result = await axios(
            'http://api-spider.azurewebsites.net/servicename',
          );
     
          setNewData(result.data);
        };
     
        fetchData();
      }, []);


    const data = React.useMemo(
      () => [
        {
          label: 'Series 1',
          data: [{ x: 1, y: 10 }, { x: 2, y: 10 }, { x: 3, y: 10 }]
        },
        {
          label: 'Series 2',
          data: [{ x: 1, y: 10 }, { x: 2, y: 10 }, { x: 3, y: 10 }]
        },
        {
          label: 'Series 3',
          data: [{ x: 1, y: 10 }, { x: 2, y: 10 }, { x: 3, y: 10 }]
        }
      ],
      []
    )
   
    const axes = React.useMemo(
      () => [
        { primary: true, type: 'linear', position: 'bottom' },
        { type: 'linear', position: 'left' }
      ],
      []
    )
   
   console.log(newData)
    return (
      <div
        style={{
          width: '400px',
          height: '300px'
        }}
      >
        <Chart data={data} axes={axes} />
        
      </div>
    )
  }