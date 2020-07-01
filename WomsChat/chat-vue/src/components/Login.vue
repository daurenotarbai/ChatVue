<template>
  <div>
    <input v-model="login" placeholder="Login" type="text">
    <input v-model="password" placeholder="Password" type="password">
    <button @click="setlogin">Sign In</button>
    <br>
    {{login}}
    {{password}}
  </div>
</template>

<script>
// import $ from 'jquery'

export default {
  name:"Login",
  data(){
    return{
      login:'',
      password:'',
    }
  },
  methods:{
    setlogin(){
      $.ajax({
        url:"http://127.0.0.1:8000/auth/token/login/",
        type:"POST",
        data:{
          username:this.login,
          password:this.password
        },
        success:(response)=>{
          console.log(response)
          alert("Thank you for with us")
          sessionStorage.setItem("auth_token",response.data.attributes.auth_token)
          this.$router.push({name:"home"})
        },
        error:(response)=>{
          if(response.status===400){
            alert("Login or password is not correct")
          }

          console.log(response)
        }
        

      })
    }, 
  }
  
}
</script>

<style scoped>

</style>