import React, {useState, useEffect} from "react"
import axios from "axios"
import { DataGrid, GridToolbar } from '@material-ui/data-grid';


const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'subscriptionname', headerName: 'Service name', width: 250 },
    { field: 'servicename', headerName: 'Subscription Name', width: 250 },
    { field: 'date', headerName: 'Date ', width: 150 },
    { field: 'quantity', headerName: 'Quantity',type: 'number', width: 150 },
    { field: 'cost', headerName: 'Cost', type: 'number', width: 150 },
    {
      field: 'fullName',
      headerName: 'Total cost',
      description: 'This column has a value getter and is not sortable.',
      sortable: false,
      width: 160,
      valueGetter: (params) =>
        `${params.getValue('quantity') * params.getValue('cost') || ''}`,
    },
  ];




export default function Dgrid(props) {
    const [data, setData] = useState([]);
    const [myloading, setLoading] = useState(true);
    
    useEffect(() => {
      const fetchData = async () => {
        const result = await axios(
          'http://api-spider.azurewebsites.net/servicename',
        );
   
        setData(result.data);
        setLoading(false)
      };
   
      fetchData();
    }, []);
   
    return (
        <>
        <div className="datagrid" style={{ display: props.vision}}>
        <DataGrid rows={data} columns={columns} pageSize={10} checkboxSelection loading={myloading}   components={{
    Toolbar: GridToolbar,
  }} columnBuffer={5} />
      </div>
      </>
    );
  }
   