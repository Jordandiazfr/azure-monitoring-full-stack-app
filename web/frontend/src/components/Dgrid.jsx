import React, {useState, useEffect} from "react"
import axios from "axios"
import { DataGrid } from '@material-ui/data-grid';


const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'subscriptionname', headerName: 'Service name', width: 250 },
    { field: 'servicename', headerName: 'Subscription Name', width: 250 },
    { field: 'date', headerName: 'Date ', width: 150 },
    { field: 'quantity', headerName: 'Quantity',type: 'number', width: 150 },
    { field: 'cost', headerName: 'Cost', type: 'number', width: 150 },
    {
      field: 'fullName',
      headerName: 'Full name',
      description: 'This column has a value getter and is not sortable.',
      sortable: false,
      width: 160,
      valueGetter: (params) =>
        `${params.getValue('firstName') || ''} ${params.getValue('lastName') || ''}`,
    },
  ];




export default function Dgrid() {
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
        <>
        <div style={{ height: 800, width: '100%' }}>
        <DataGrid rows={data} columns={columns} pageSize={10} checkboxSelection />
      </div>
      </>
    );
  }
   