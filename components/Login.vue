<template>
  <div class="container">
    <h1>Login</h1>
    <form action="#" method="post" v-on:submit.prevent="sendlogin()">
      <label for="usuario">Usuário</label>
      <input type="text" v-model="login.username" id="usuario" required />

      <label for="password">Senha</label>
      <input type="password" v-model="login.password" id="password" required />

      <button type="submit">Acessar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      // login: [],
      login: {
        // para o funcionamento da autenticação, as variáveis DEVEM ser 'username' e 'password'
        username: null,
        password: null,
      },
    };
  },
  methods: {
    sendlogin() {
      this.$auth
        .loginWith("local", { data: this.login })
        .then(() => {
          console.log("login autenticado com sucesso");
        })
        .catch((error) => {
          console.log("login falhou");
          console.log(error);
        });
    },
  },
};
</script>

<style>
.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #fff;
}
form {
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
