//SP20-BCS-047
//Muhammad Talha Azeem
import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { TextInput } from 'react-native-web';

export default function Login(){
    return(
        <View style={styles.container}>
            <View style={styles.MiniContainer}>
                    <Text style={{color:"white",fontWeight:"700"}}> MEDDU</Text>
            </View>
            <View style={styles.FormConatiner}>
                <Text style={{color:"blue", fontSize:23,fontWeight:"800"}}>Signup</Text>
                
                <TextInput type="text" placeholder="First Name" style={styles.TextInput} />
                <TextInput type="text" placeholder="Last Name" style={styles.TextInput} />
                <TextInput type="email" placeholder="Email" style={styles.TextInput} />
                <TextInput type="Password" placeholder="****"  securetextentery={true} style={styles.TextInput} />
                <TextInput type="Password" placeholder="Confirm Password"  securetextentery={true} style={styles.TextInput} />
                <TextInput type="text" placeholder="Gender" style={styles.TextInput} />
                <TextInput type="number" placeholder="Age" style={styles.TextInput} />
                <TextInput type="text" placeholder="Country" style={styles.TextInput} />
                <TextInput type="text" placeholder="City" style={styles.TextInput} />
                <TextInput type="text" placeholder="Street" style={styles.TextInput} />
           <TouchableOpacity style={{color:"blue", fontSize:12,padding:8,marginLeft:"33%"}}>Forget your Password</TouchableOpacity>
           <TouchableOpacity style={{color:"#fff",fontWeight:"bold",borderRadius:"30%",backgroundColor:"blue", fontSize:25,paddingLeft:30,paddingRight:30,padding:12,marginTop:"3%"}}>Signup</TouchableOpacity>
           <TouchableOpacity style={{color:"blue", fontSize:12,padding:5}}>Have an account? Login</TouchableOpacity>
           
            </View>

        </View>
    )
}
const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
         backgroundColor:"#eee"
      },
      MiniContainer:{
        alignItems:"center",
        justifyContent:"center",
        width:"100%",
        height:"20%",
        backgroundColor:"blue",
        borderBottomLeftRadius:20,
        borderBottomRightRadius:20
      },
      FormConatiner:{
        position:"absolute",
        top:"15%",
        justifyContent:"center",
        alignItems:"center",
        borderRadius:25,
        marginHorizontal :"10%",
        backgroundColor:"#fff",
        height:"80%",
        width:"92%",
        marginBottom:"10%",
        elevation:45,
        
      },
      TextInput:{
        
        borderColor:"blue",
        borderBottomWidth:2,
        padding:"3%"
      }
})