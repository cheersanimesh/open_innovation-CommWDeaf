import axios from 'axios';
const instance=axios.create({
    baseURL:"192.168.122.21:4000"
})


export default instance;