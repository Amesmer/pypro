import{_ as e,h as n,i as a,f as s,o as t,b as r,D as d,a as i,j as o,k as c}from"./index-e837eef9.js";const p={class:"app-container center"};const u=e({},[["render",function(e,r){const d=s("el-empty");return t(),n("div",p,[a(d,{description:"Admin 权限可见"})])}],["__scopeId","data-v-5a78679f"]]),l={class:"app-container center"};const m=e({},[["render",function(e,r){const d=s("el-empty");return t(),n("div",l,[a(d,{description:"Editor 权限可见"})])}],["__scopeId","data-v-f3d24ef0"]]),f=r({__name:"index",setup(e){const n=d(),a=i("admin");return n.roles.includes("admin")||(a.value="editor"),(e,n)=>(t(),o(c("admin"===a.value?u:m)))}});export{f as default};
