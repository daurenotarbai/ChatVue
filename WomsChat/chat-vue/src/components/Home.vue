<template>
  <mu-container>

    <mu-appbar style="width: 100%;" color="primary">
       Chat on VueJS
      <mu-button flat slot="right" v-if="!auth" @click="gologin">Sign in</mu-button>
      
      <mu-button flat slot="right" v-else @click="logout">Sign Out </mu-button>

    </mu-appbar>
    <mu-row>
      <h1></h1>
    </mu-row>  
    <!-- <mu-row>
      <Room v-if="auth" @goDialog="goDialog"></Room>
      <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
      <Dialog v-if="!dialog.show"></Dialog>
    </mu-row> -->

    <slot></slot>

  </mu-container>
</template>

<script>

// import Room from '@/components/rooms/Room.vue'
// import Dialog from '@/components/rooms/Dialog'
export default {
  name:"Home",
  // components: {
  //   Room,
  //   Dialog
  // },
  data(){
    return {
      dialog: {
        id: '',
        show: false,
      }
    }
  },
  computed:{
    auth(){
      if(sessionStorage.getItem("auth_token")){
        return true
      }
    }
  },
  methods:{
    gologin(){
      this.$router.push({name:"login"})
    },
    logout(){
      sessionStorage.removeItem("auth_token")
      window.location ='/' 
    },
    // goDialog(id){

    //   this.dialog.id = id
    //   this.dialog.show = true

    // }
  },
  
}

</script>

<style scoped>
  .dialog{
    border-right: 3px solid rgb(33, 150, 243);
    border-bottom: 3px solid rgb(33, 150, 243);
    border:3px solid rgb(33, 150, 243);
    height: 430px;

    overflow-y: scroll;

  

  } 


</style>