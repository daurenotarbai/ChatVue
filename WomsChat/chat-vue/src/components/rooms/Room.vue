<template>
  <HomeSlot>
    <mu-row>
        <mu-col class="room-list" span="4" xl="2">
          <mu-button @click="createRoom">Create Room</mu-button> 
          <div v-for="room in rooms">
              <h2><p @click="goDialog(room.id)">{{room.creater.username}}</p></h2>
          </div>
        </mu-col>
        <slot></slot>
    </mu-row>
  </HomeSlot>

</template>
<script>
import HomeSlot from '../Home'




export default {
  name: "Room",
  components:{
    HomeSlot,
  },

  data(){
    return{
      rooms:'',
      
    }
  },
  created(){
    $.ajaxSetup({
      headers:{'Authorization':"Token " + sessionStorage.getItem('auth_token')},
    });
    this.loadRoom()
  },
  methods: {
    loadRoom(){
      $.ajax({
        url:"http://127.0.0.1:8000/api/v1/chat/room/",
        type: "GET",
        success:(response)=>{
          this.rooms = response.data.data
        },
        error:(response)=>{
          console.log(response)
        }
      })
    },
    goDialog(id){
      // this.$emit("goDialog",id)
      this.$router.push({name:'dialog',params:{id:id}})

    },
    createRoom(){
      $.ajax({
        url:"http://127.0.0.1:8000/api/v1/chat/room/",
        type: "POST",
        success:(response)=>{
          this.loadRoom
        },
        error:(response)=>{
          alert(response.statusText)
        }
      })

    }
  }
  
}
</script>
<style scoped>
.room{
  border: 3px solid rgb(33, 150, 243);
  height: 560px;

  
}
.room-list{
  box-shadow: 0px 2px 3px rgb(33, 150, 243);
}
/* .rooms-list {
    margin: 0 10px 0 0;
    box-shadow: 1px 4px 5px #848181;
} */
</style>