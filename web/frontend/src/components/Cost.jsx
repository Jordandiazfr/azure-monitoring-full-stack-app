import React, {useState, useEffect} from "react"
import axios from "axios"

export default function Cost() {
    const [data, setData] = useState([]);
   
    useEffect(() => {
      const fetchData = async () => {
        const result = await axios(
          'http://localhost:4000/servicename',
        );
   
        setData(result.data);
      };
   
      fetchData();
    }, []);
   
    return (
      <div>
      <table> 
      <thead>
          <tr>
              <th>Subscription Name</th>
              <th>Date</th>
              <th>Service name</th>
              <th>Service Resource</th>
              <th>Quantity</th>
              <th> Cost </th>
          </tr>
      </thead>
      <tbody> 
      {console.log(data)}
        {data.map(item => (
    
        <tr key={item.id}> 
          <td> {item.subscriptionname} </td>
          <td> {item.date} </td>
          <td> {item.servicename} </td> 
          <td> {item.serviceresource} </td>
          <td> {item.quantity} </td>
          <td> {item.cost} </td>
        </tr>

        ))}
        </tbody>
        </table>
      </div>
    );
  }
   