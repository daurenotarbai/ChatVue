<template>
  <RoomSlot>
    <mu-col span="8" xl="10">
      <AddUsers :room="id"></AddUsers>
      <mu-container class="dialog" >
        <mu-row  v-for="dialog in dialogs" direction="column" justify-content="start" align-items="end"  :key="dialog.id" >
          <p><strong>{{dialog.user.username}}</strong></p>
          <p>{{dialog.text}}</p>
          <span>{{dialog.date}}</span>
        </mu-row>
      </mu-container>
      <mu-container>
        <mu-row>
            <mu-text-field v-model="form.textarea" label="Send Message" color="blue" full-width></mu-text-field>
            <mu-button round @click="sendMess" color="blue">Send</mu-button>
        </mu-row>
      </mu-container>
      
    </mu-col>
  </RoomSlot>
</template>

<script>

  import RoomSlot from './Room'
  import AddUsers from './AddUsers'
  

  export default {

    name: "Dialog",

    props: {
      id:'',
      },
    components:{
      AddUsers,
      RoomSlot
    },
    data() {
      return {
        dialogs:'',
        form:{
          textarea:''}
      }
    },
    mounted(){
      this.loadDialog()
    }, 

    created(){
      $.ajaxSetup({
        headers:{'Authorization':"Token " + sessionStorage.getItem('auth_token')},
      });
      this.loadDialog()

      setInterval(() =>{
         this.loadDialog()

      }, 4000)

    },

    methods: {

      loadDialog(){
        $.ajax({
          url:"http://127.0.0.1:8000/api/v1/chat/dialog/",
          type: "GET",
          data: {
            room: this.$route.params.id
          },
          success:(response)=>{
            this.dialogs = response.data.data
          }
        })
      },
      sendMess(){
        $.ajax({
          url:"http://127.0.0.1:8000/api/v1/chat/dialog/",
          type: "POST",
          data: {
            room: this.$route.params.id,
            text: this.form.textarea
          },
          success:(response)=>{
            console.log(response)
            this.dialogs = response.data.data
            this.form.textarea = ''
            this.loadDialog()
          }
        })

      }
      

      } 
    }



</script>

<style>
  .dialog{
    border-right: 3px solid rgb(33, 150, 243);
    border-bottom: 3px solid rgb(33, 150, 243);
    border:3px solid rgb(33, 150, 243);
    height: 430px;
    overflow-y: scroll;

  } 
    /* .dialog {
        border: 1px solid #000;
    } */

</style>
